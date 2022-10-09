import itertools
import math
import time
from pathlib import Path
from typing import Optional

import sbol3
from sbol_utilities.component import dna_component_with_sequence

import excel_helpers

EXCEL_FILE = Path('gfp-scanning-library.xlsx')
SBOL_OUTPUT_FILE = Path('gfp-scanning-library.nt')

start_time = time.time()
# load a sequence and variation table from the Excel file
print('Reading Excel table')
library_name, original_sequence, variant_lists = excel_helpers.read_variant_table(EXCEL_FILE)
# In the example file, there should be 239*21 = 5019 variants all told across all site lists

# Now, use the variant tables to create the SBOL model
print('Creating SBOL document')
doc = sbol3.Document()
sbol3.set_namespace('http://bbn.com/examples')
library_id = sbol3.string_to_display_id(library_name)

# First, create a Component for the original sequence
print('Creating Component for original sequence')
original, seq = dna_component_with_sequence(f'{library_id}_original', original_sequence)
doc.add([original, seq])


# Second, create a Component for each amino acid option (including stop and delete, if they are used)
print('Creating Components for amino acids replacements')
all_aa_variants = sorted(set(itertools.chain(*variant_lists)))  # should be up to 22 different values
# Each pair has a Component and its associated sequence
aa_pairs = {aa: dna_component_with_sequence(sbol3.string_to_display_id(f'amino_acid_{aa}'), '' if aa == 'DEL' else aa)
            for aa in all_aa_variants}
# add them all to the document, then make a list of just the components
doc.add(list(itertools.chain(*aa_pairs.values())))
aa_components = {aa: pair[0] for aa, pair in aa_pairs.items()}
print(f'Created {len(aa_components)} Components for amino acid replacements')


# Third, make a collection for each distinct set of variants to be used
def variant_set_name(variant_set):
    return 'variants_'+''.join(variant_set)
# In the example file, there should be 21 collections: one per replaced sequence value (20 amino acids and stop codon)
print('Creating Collections for each distinct set of variants')
variant_collections = dict()
for variants in variant_lists:
    set_name = variant_set_name(variants)
    if set_name not in variant_collections:
        collection = sbol3.Collection(sbol3.string_to_display_id(set_name),
                                      members=[aa_components[aa] for aa in variants])
        variant_collections[set_name] = collection
doc.add(list(variant_collections.values()))
print(f'Created {len(variant_collections)} Collections for sets of variants')


def add_adjacent_to_last_feature(component: sbol3.Component, feature: sbol3.Feature) -> sbol3.Feature:
    """Add a Feature to a Component, and indicate adjacency by linking to the last
    feature (if any) via a Meets constraint

    :param component: Component to add to
    :param feature: Feature to be added
    :return: pass-through return of feature
    """
    last_feature = component.features[-1] if component.features else None
    component.features.append(feature)
    if last_feature:  # if there is no last feature, the constraint is moot
        meets_constraint = sbol3.Constraint(sbol3.SBOL_MEETS, last_feature, feature)
        component.constraints.append(meets_constraint)
    return feature

# Fourth, make the template Component that will be used uniformly for the library
# This will have a SubComponent for each non-varied region and a SubComponent for each varied amino acid
print('Creating site variant template and per-site libraries')
template = sbol3.Component(f'{library_id}_template', types=[sbol3.SBO_DNA])
doc.add(template)
per_site_libraries = []
variables: dict[int, sbol3.Feature] = dict()
current_fixed_region: Optional[sbol3.SubComponent] = None
for variants, index in zip(variant_lists, range(1, len(original_sequence)+1)):
    if variants:  # if this is a variable region, add a variable
        current_fixed_region = None
        location = sbol3.Range(start=index, end=index, sequence=original.sequences[0])
        variable = sbol3.SubComponent(original, source_locations=[location])
        add_adjacent_to_last_feature(template, variable)
        variable_feature = sbol3.VariableFeature(cardinality=sbol3.SBOL_ONE, variable=variable,
                                                 variant_collections=[variant_collections[variant_set_name(variants)]])
        per_site_libraries.append(sbol3.CombinatorialDerivation(f'{library_id}_{index}', name=f'{library_id}_{index}',
                                                                template=template, strategy=sbol3.SBOL_ENUMERATE,
                                                                variable_features=[variable_feature]))
    else:  # otherwise, start or extend a fixed region
        if not current_fixed_region:
            location = sbol3.Range(start=index, end=index, sequence=original.sequences[0])
            current_fixed_region = sbol3.SubComponent(original, source_locations=[location])
            add_adjacent_to_last_feature(template, current_fixed_region)
        else:
            current_fixed_region.source_locations[0].end = index
doc.add(per_site_libraries)
print(f'Created variation plans for {len(per_site_libraries)} individual sites')

# Finally, create one top-level CombinatorialDerivation that contains all of the others
print('Creating all-site library')
meta_variable = sbol3.LocalSubComponent(types=[sbol3.SBO_DNA])
meta_template = sbol3.Component(f'{library_id}_meta_template', types=[sbol3.SBO_DNA], features=[meta_variable])
doc.add(meta_template)
meta_variable_feature = sbol3.VariableFeature(cardinality=sbol3.SBOL_ONE, variable=meta_variable,
                                              variant_derivations=per_site_libraries)
site_variant_library = sbol3.CombinatorialDerivation(library_id, name=library_name, template=meta_template,
                                                     variable_features=[meta_variable_feature])
doc.add(site_variant_library)

# And validate and write the SBOL file
print('Document complete: checking validity')
report = doc.validate()
if report:
    raise ValueError(f'Document produced was not valid: found {len(report)} errors or warnings')

print(f'Writing document to {SBOL_OUTPUT_FILE}')
doc.write(str(SBOL_OUTPUT_FILE), sbol3.SORTED_NTRIPLES)
print('Document written')

print(f'Total elapsed time: {math.trunc(10*(time.time()-start_time))/10} seconds')
