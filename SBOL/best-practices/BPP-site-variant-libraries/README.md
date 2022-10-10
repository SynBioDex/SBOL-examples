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

For a scanning library, the key challenge is to indicate that when one site is changed, another site should not be changed. This can be implemented using two layers of `CombinatorialDerivation` objects:

 - For each site, a `CombinatorialDerivation` specifies the subset of sequences that vary that specific site. There is one such `CombinatorialDerivation` for every site.
 - The per-site libraries are then used as `variantDerivation` values for a higher-level `CombinatorialDerivation`, thereby collectively describing a library that considers each site in turn.

This representation can be made more efficient by sharing `template` and `variantCollection` values across the single-site libraries.  Specifically:

- Consider the set of all values that are used by _any_ individual site and create a `Component` for each of these. For example, a site variant library for amino acids would have 20 values if every amino acid was an option in at least one site.
  - Deletions and insertions can be included in the set of values by either using a `Component` with a length zero sequence or a variable with the `SBOL:zeroOrOne` cardinality rather than the `SBOL:one` cardinality.
- The same set of variations is likely to be used multipled times, e.g., varying every A amino acid to "everything amino acid except for A". To this end, create a `Collection` for each distinct set of variations. 

**[put a diagram here showing some variant libraries]**

- The template consists of a chain of `SubComponent` features linked together with `Constraint` objects of type `SBOL:meets`. Each is an `instance_of` a `Component` for the original gene the library is based on and uses the `sourceLocation` property to select the portion of the gene it represents.
  - The location of each site being varied is a `Range` covering that specific site.
  - Each regions that is not being varied is represented by a `SubComponent` spanning the `Range` between variation sites.

**[put a diagram here showing a template based on the combinatorial example]**

- For each site being varied, create a per-site `CombinatorialDerivation`:
  - The `strategy` property should be `SBOL:enumerate`
  - The `template` should be the shared template `Component`
  - There should be one `VariableFeature` whose `variable` is the template's `SubComponent` for the site, whose cardinality is `SBOL:one` (unless representing deletion or insertion via cardinality) and whose `variantCollection` points to the `Collection` of values for that site.

- The higher-level `CombinatorialDerivation` should be:
  - The `strategy` property should be `SBOL:enumerate`
  - The `template` should be a placeholder `Component` with one `LocalSubComponent` feature.
  - There should be one `VariableFeature` whose `variable` is the one feature in the template, and whose `variantDerivation` property is all the per-site `CombinatorialDerivation` objects as its values.


### 2.2 Combinatorial Libraries <a name="combinatorial"></a>

Combinatorial libraries are simpler to represent than scanning libraries, since there is no constraint limiting the number of sites that vary. A combinatorial library is thus represented exactly like the variation of a single site, except that there are multiple variables rather than one variable.

## 3. Example Files <a name='examples'></a>

Examples are provided in the curated examples collection directory [site-variant-libraries](../../curated-examples/site-variant-libraries/). 

Specifically, for both combinatorial and scanning libraries, we provide:

* an Excel spreadsheet specifying a combinatorial library and another specifying a scanning library, 
* a Python script that uses [SBOL-utilities](https://www.github.com/SynBioDex/SBOL-utilities) to convert the library-specifying Excel files into SBOL files, 
* for each library, an SBOL output from the script containing its specification, 

For more information, see the directory [README](../../curated-examples/site-variant-libraries/README.md). 

<There will also be a Python script that compute the expansion of each library into specific constructs an exports them in both SBOL and FASTA formats. Currently, however, SBOL-utilities has bugs that are being triggered in the sequence calculation, so the final expansions that are computed is not correct. There is also an issue with slowness. The known issues are:>

<The sequence calculator is ignoring sourceLocation, so it's putting in extra copies of the sequence>
<Deletions are not being handled correctly. Currently, they are represented as length zero sequences. A better way would be to make it a "zero or one" variable, but expand-CDs probably isn't handling that yet either.>
<ExpandCDs is requiring that things have names for its debugging logging, which shouldn't be running anyway. Need to fix both aspects of that.>
<Creating new copies of the template becomes very slow over time, due to the deep cloning not being smart about copying contents.>


## 4. Relationship to Other BPPs <a name='relations'></a>

This BPP is not explicitly related to any other prior or pending BPPs.

## 5. Discussion <a name='discussion'></a>

For representing scanning libraries, several other potential models were considered besides the one finally presented. Here we will summarize each other significant alternative briefly, and why it was found less preferable than the one ultimately presented:

* The strategy could be a special "vary only one variable at a time" value. This would require expansion tools to understand.
* Each site could have its own template
* We could scan by using a variantMeasure to indicate changes to start and end values
* Rather than using variantCollections, we could point directly to the alternatives with variant properties
* We could make an alternative where we use the Sequence rather than a Component for the template
* Adding constraints that say that one site shouldn't vary if another does.











