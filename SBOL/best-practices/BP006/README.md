# BP 006 -- Recommended Ontologies for External Terms

External ontologies and controlled vocabularies are an integral part of SBOL. SBOL uses *IRIs* (typically *URLs* to access existing biological information through these resources.
New SBOL-specific terms are defined only when necessary.
For example, `Component types`, such as DNA or protein, are described using Systems Biology Ontology (SBO) terms. Similarly, the `roles` of a DNA or RNA `Component are described via Sequence Ontology (SO) terms. Although RECOMMENDED ontologies have been indicated in relevant sections where possible, other resources providing similar terms can also be used. A summary of these external sources can be found in the table below.

| **SBOL Entity** | **Property** | **Preferred External Resource** | **More Information** |
| --------------- | ------------ | ------------------------------- | -------------------- |
| **Component** | type | SBO (physical entity branch) | http://www.ebi.ac.uk/sbo/main/  |
|| type | SO (nucleic acid topology) | http://www.sequenceontology.org  |
|| role | SO (*DNA* or *RNA*) | http://www.sequenceontology.org     |
|| role | CHEBI (*small molecule*) | https://www.ebi.ac.uk/chebi/     |
|| role | PubChem (*small molecule*) | https://pubchem.ncbi.nlm.nih.gov/   |
|| role | UniProt (*protein*) | https://www.uniprot.org/       |
|| role | NCIT (*samples*) | https://ncithesaurus.nci.nih.gov/       |
| **Interaction** | type | SBO (occurring entity branch) | http://www.ebi.ac.uk/sbo/main/|
| **Participation** | role | SBO (participant roles branch) | http://www.ebi.ac.uk/sbo/main/  |
| **Model** | language | EDAM | http://bioportal.bioontology.org/ontologies/EDAM       |
|| framework | SBO (modeling framework branch) | http://www.ebi.ac.uk/sbo/main/  |
| **om:Measure** | type | SBO (systems description parameters) | http://www.ebi.ac.uk/sbo/main/ |

Preferred external resources from which to draw values for various SBOL properties.


The IRIs for ontological terms SHOULD be URLs from identifiers.org.  However, it is acceptable to use terms from purl.org as an alternative, for example when RDF tooling requires URLs to be represented as compliant QNames.  SBOL software may convert between these forms as required.
