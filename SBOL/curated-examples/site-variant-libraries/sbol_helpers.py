import sbol3


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
