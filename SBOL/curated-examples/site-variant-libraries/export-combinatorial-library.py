import math
import time
from pathlib import Path
from typing import Optional

import sbol3
from sbol_utilities.component import protein_component_with_sequence

import excel_sbol_utils.helpers as excel_helpers
import sbol_helpers

EXCEL_FILE = Path('gfp-combinatorial-library.xlsx')
SBOL_OUTPUT_FILE = Path('gfp-combinatorial-library.nt')

start_time = time.time()
# load a sequence and variation table from the Excel file
print('Reading Excel table')
library_name, original_sequence, variant_lists = excel_helpers.read_variant_table(EXCEL_FILE)
# In the example file, there should be 10*10*10*10*9 = 90,000 variants across all combinations
print(f'Library specifies a total of {math.prod(len(variants) for variants in variant_lists if variants)} variants')

# Now, use the variant tables to create the SBOL model
print('Creating SBOL document')
doc = sbol3.Document()
sbol3.set_namespace('http://bbn.com/examples')
library_id = sbol3.string_to_display_id(library_name)

# First, create a Component for the original sequence
print('Creating Component for original sequence')
original, seq = protein_component_with_sequence(f'{library_id}_original', original_sequence)
doc.add([original, seq])

# Second, create a Component for each amino acid option (including stop and delete, if they are used)
# In the example file, there should be 11 values
print('Creating Components for amino acids replacements')
aa_components = sbol_helpers.aa_component_table(doc, variant_lists)
print(f'Created {len(aa_components)} Components for amino acid replacements')


# Third, make a collection for each distinct set of variants to be used
# In the example file, there should be 4 collections
print('Creating Collections for each distinct set of variants')
variant_collections = sbol_helpers.make_variant_collections(doc, variant_lists, aa_components)
print(list(variant_collections.keys()))
print(f'Created {len(variant_collections)} Collections for sets of variants')


# Fourth, make the template Component that will be used uniformly for the library
# This will have a SubComponent for each non-varied region and a SubComponent for each varied amino acid
# Also make the combinatorial derivation that expresses combinations of sites
print('Creating site variant library and template')
template = sbol3.Component(f'{library_id}_template', types=[sbol3.SBO_PROTEIN])
doc.add(template)
site_variant_library = sbol3.CombinatorialDerivation(library_id, name=library_name, template=template,
                                                     strategy=sbol3.SBOL_ENUMERATE)
doc.add(site_variant_library)
current_fixed_region: Optional[sbol3.SubComponent] = None
for variants, index in zip(variant_lists, range(1, len(original_sequence)+1)):
    if variants:  # if this is a variable region, add a variable
        current_fixed_region = None
        location = sbol3.Range(start=index, end=index, sequence=original.sequences[0])
        # These are LocalSubComponent rather than plain SubComponent because they are always replaced
        variable = sbol3.LocalSubComponent(types=[sbol3.SBO_PROTEIN])
        sbol_helpers.add_adjacent_to_last_feature(template, variable)
        variant_collection = variant_collections[sbol_helpers.variant_set_name(variants)]
        variable_feature = sbol3.VariableFeature(cardinality=sbol3.SBOL_ONE, variable=variable,
                                                 variant_collections=[variant_collection])
        site_variant_library.variable_features.append(variable_feature)
    else:  # otherwise, start or extend a fixed region
        if not current_fixed_region:
            location = sbol3.Range(start=index, end=index, sequence=original.sequences[0])
            current_fixed_region = sbol3.SubComponent(original, source_locations=[location])
            sbol_helpers.add_adjacent_to_last_feature(template, current_fixed_region)
        else:
            current_fixed_region.source_locations[0].end = index
print(f'Created combined variation plan for {len(site_variant_library.variable_features)} sites')

# And validate and write the SBOL file
print('Document complete: checking validity')
report = doc.validate()
if report:
    raise ValueError(f'Document produced was not valid: found {len(report)} errors or warnings')

print(f'Writing document to {SBOL_OUTPUT_FILE}')
doc.write(str(SBOL_OUTPUT_FILE), sbol3.SORTED_NTRIPLES)
print('Document written')

print(f'Total elapsed time: {math.trunc(10*(time.time()-start_time))/10} seconds')
