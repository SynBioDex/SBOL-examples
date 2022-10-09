import itertools

import sbol3
from sbol_utilities.component import protein_component_with_sequence


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


def variant_set_name(variant_set: list[str]) -> str:
    """Create a name for an amino acid variant set by concatenating the sorted names of the amino acids

    :param variant_set: list of amino acid variants, assumed to be in a consistent fixed order
    :return: string to use as the name for the set
    """
    return 'variants_'+''.join(variant_set)


def aa_component_table(doc: sbol3.Document, variant_lists: list[list[str]]) -> dict[str: sbol3.Component]:
    """Create components for all the amino acids (or stop or deletion) that will be used in creating variants
    Each one is an amino acid component and associated sequence (containing only 0 or 1 residue)

    :param doc: Document to which components will be added
    :param variant_lists: list of all variant sets that will be used
    :return: dictionary mapping variant name to Component
    """
    all_aa_variants = sorted(set(itertools.chain(*variant_lists)))  # should be up to 22 different values
    # Each pair has a Component and its associated sequence
    aa_pairs = {aa: protein_component_with_sequence(sbol3.string_to_display_id(f'amino_acid_{aa}'),
                                                    sequence='' if aa == 'DEL' else aa)
                for aa in all_aa_variants}
    # add them all to the document, then make a list of just the components
    doc.add(list(itertools.chain(*aa_pairs.values())))
    return {aa: pair[0] for aa, pair in aa_pairs.items()}


def make_variant_collections(doc: sbol3.Document, variant_lists: list[list[str]],
                             aa_components: dict[str, sbol3.Component]) -> dict[str, sbol3.Collection]:
    """Create an SBOL Collection for each distinct set of variant values (amino acids, stop codons, or deletions)
    that will be substituted at some site, e.g., "everything but A", "everything but W". These will then be
    reused for every site with the same set of values, e.g., every A that will be replaced by "everything but A"

    :param doc: Document to which components will be added
    :param variant_lists: list of all variant sets that will be used
    :param aa_components: dictionary mapping variant names to the Components that will make up the sets
    :return: dictionary mapping variant set name to Collection
    """
    variant_collections = dict()
    for variants in variant_lists:
        set_name = variant_set_name(variants)
        if set_name not in variant_collections:
            collection = sbol3.Collection(sbol3.string_to_display_id(set_name),
                                          members=[aa_components[aa] for aa in variants])
            variant_collections[set_name] = collection
    doc.add(list(variant_collections.values()))
    return variant_collections
