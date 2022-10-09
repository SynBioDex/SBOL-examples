# Representing Site Variant Libraries

These examples show how to representing libraries of nucleic acid or amino acid constructs that are varied at the level of individual base pairs or residues.

These examples show how to implement both a "scanning" library that varies each site independently and a combinatorial library that varies several sites together.


## Setup

You will need Python 3.8+ and the packages listed in the requirements file:

```
pip3 install -r requirements.txt
```

## Running the scripts

There are two scripts to run:

```
python3 export-scanning-library.py 
python3 export-combinatorial-library.py 
```

These scripts use shared code in the "helpers" files. 
Each turns an Excel file into an SBOL3 representation, which is saved to an RDF file in sorted N-triples format. 
As the scripts run, they explain what they are doing.

You can experiment with variations by changing the wildtype DNA sequence (cell C14), the options section (C31:C35), and the amino acid table.
