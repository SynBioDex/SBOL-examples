BPP -- Representation of Site Variant Libraries
===================================


BP                     | <leave empty>
----------------------|--------------
**Title**                | Representation of Site Variant Libraries
**Authors**           | Jacob Beal (jakebeal@ieee.org), James Diggans, Chris Myers, Jet Mante, Lukas Buecherl, _anybody else?_
**SBOL Version** | SBOL 3.0.1 and later
**Replaces**        | None
**Approved**          | 

Abstract
-----------

This Best Practice Proposal presents a set of practices for representing libraries of nucleic acid or amino acid constructs that are varied at the level of individual base pairs or residues. These practices and examples can be applied to libraries that consider both "scanning" libraries, in which a large number of sites are changed separately, and combinatorial libraries, in which multiple sites are changed at the same time.


Table of Contents
---------------------

* [1. Rationale](#rationale)
* [2. Description](#description)
  * [2.1 Scanning Libraries](#scanning)
  * [2.2 Combinatorial Libraries](#combinatorial)
* [3. Example Files](#examples)
* [4. Relationship to other BPPs](#relations)
* [5. Discussion](#discussion)

## 1. Rationale <a name="rationale"></a>

One strategy often used in seeking to understand or engineer a gene is to construct a site variant library that "scans" along the gene, perturbing each location individually, e.g., changing the amino acid at each site, changing the codon for each amino acid, making a deletion at each site, or inserting stop codon at each site. Significant sites and their properties can then be determined by observing which variants exhibit significantly different behavior than the base sequence.

For example, a scanning site-variant libarary that modifies GFP (a 239 amino acid protein) by considering every single-amino-acid replacement would consist of 4,541 different sequences (from 20 possible amino acids, 19 replacements at each site times 239 sites).

Another class of library, often used once sites of interest have been identified, considers the combinatorial variation of sites, in which multiple sites are changed at the same time. For example a combinatorial library might consider GFP modified using all 20 possible amino acids at four sites, for a total of 160,000 different sequences (20 to the 4th power).

Communicating about such libraries has often been difficult and ambiguous, however, so it is valuable to have an unambiguous representation in SBOL. Importantly, SBOL's `CombinatorialDerivation` class is explicitly designed for representing libraries, but the examples previously presented have been applied to representing combinations at the level of parts, rather than individual amino acids. Moreover, given the flexibility of the representation, there is more than one possible strategy for representing these libraries.

For these reasons, this Best Practice Proposal sets out of a set of practices for representing libraries of nucleic acid or amino acid constructs, along with examples of how these may be applied to both scanning libraries and combinatorial libraries.

## 2. Description <a name="description"></a>

### 2.1 Scanning Libraries <a name="scanning"></a>

### 2.2 Combinatorial Libraries <a name="combinatorial"></a>

Combinatorial libraries are simpler to represent than scanning libraries, since there is no constraint limiting the number of sites that vary. A combinatorial library is thus represented exactly like the variation of a single site, except that there are multiple variables rather than one variable.

For example, the attached diagram shows a variation of GFP 

## 3. Example Files <a name='examples'></a>

Examples are provided in the curated examples collection directory [site-variant-libraries](../../curated-examples/site-variant-libraries/). 

Specifically, for both combinatorial and scanning libraries, we provide:

* an Excel spreadsheet specifying a combinatorial library and another specifying a scanning library, 
* a Python script that uses [SBOL-utilities](https://www.github.com/SynBioDex/SBOL-utilities) to convert the library-specifying Excel files into SBOL files, 
* for each library, an SBOL output from the script containing its specification, 
* a Python script that compute the expansion of each libraries into specific constructs, 
* for each library, the final constructs generated in both SBOL and FASTA formats

For more information, see the directory [README](../../curated-examples/site-variant-libraries/README.md). 

## 4. Relationship to Other BPPs <a name='relations'></a>

This BPP is not explicitly related to any other prior or pending BPPs.

## 5. Discussion <a name='discussion'></a>

For representing scanning libraries, several other potential models were considered besides the one finally presented. Here we will summarize each other significant alternative briefly, and why it was found less preferable than the one ultimately presented:

* The strategy could be a special "vary only one variable at a time" value. This would require expansion tools to understand.
* Each site could have its own template
* We could scan by using a variantMeasure to indicate changes to start and end values
* Rather than using variantCollections, we could point directly to the alternatives with variant properties
* We could make an alternative where we use the Sequence rather than a Component for the template











