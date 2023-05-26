# BP 012 -- Annotating Scores with identity and time information

Scores in an SBOL document can be annotated with creation and modification dates, as well as with an associated identity.
We can generate an `Activity` component with the report identification and timestamp.
After adding the score to the SBOL document as a `Measure` component, we can link both objects using the `prov:wasGeneratedBy` property.
For the unit of the measurement we can use the [OM-Ontology of Units of Measure](http://www.ontology-of-units-of-measure.org) and for its type we can make use of the [EDAM - Bioscientific Data Analysis Ontology](https://bioportal.bioontology.org/ontologies/EDAM)

