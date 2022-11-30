# BP 002 -- Compliant SBOL Objects

Maintaining unique IRIs for all SBOL objects can be challenging.  To reduce this burden, users of SBOL 3.x are encouraged to follow a few simple rules when constructing IRIs and related properties for SBOL objects. When these rules are followed in constructing an SBOL object, we say that this object is *compliant*. These rules are as follows:

Compliant IRIs for `TopLevel` objects MUST conform to the following pattern:

 `<namespace>/<collection_structure>/<displayId>`


The `<namespace>` token MAY further decompose into `<domain>/<root>` tokens. The `<root>` and `<collection_structure>` tokens may optionally be omitted; alternatively, they may consist of an arbitrary number of delimiter-separated layers. Note that this pattern means that SBOL-compliant IRIs can be automatically decomposed with the aid of a `TopLevel` object's `hasNamespace` property. SBOL-compliant objects can be easily remapped into new namespaces by changing only the `<namespace>`.

Consider, for example, the SBOL-compliant *IRI*:
>https://synbiohub.org/igem/2017_distribution/promoters/constitutive/BBa_J23101

for a `Component` with a `hasNamespace` value https://synbiohub.org/igem/2017_distribution.
This *IRI* can be decomposed as follows:

> namespace: https://synbiohub.org/igem/2017_distribution  
domain: https://synbiohub.org   
root: igem/2017_distribution   
collection: promoters/constitutive   
displayId: BBa\_J23101

SBOL-compliant IRIs also facilitate auto-construction of child objects with unique *IRIs*.
Child objects of `TopLevel` objects with compliant *IRIs* MUST conform to the following pattern:   
`<parent_iri>/<child_type>/<child_type_counter>` where the `<parent_iri>` refers to the IRI of the parent object, the `<child_type>` refers to the SBOL class of the child object, and `<child_type_counter>` is a unique index for the child object.
The `<child_type_counter>` of a new object SHOULD be calculated at time of object creation as 1 + the maximum `<child_type_counter>` for each `<child_type>` object in the parent (e.g., `<parent_iri>/SequenceAnnotation37`). 
Note that numbering is independent for each type, so a `Component` can have children "SubComponent37" and "Constraint37". This best practice obviously cannot be applied to classes of IRIs that do not allow the specified structure, such as UUIDs.

All examples in this specification use compliant *IRIs*.
