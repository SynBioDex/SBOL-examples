# BP 004 -- Annotations: Embedded Objects vs. External References
When annotating an SBOL document with additional information, there are
two general methods that can be used:

- Embed the information in the SBOL document using properties outside of the SBOL namespace.
- Store the information separately and annotate the SBOL document with *IRIs* that point to it.

In theory, either method can be used in any case. (Note that a third case not
discussed here is to annotate external objects with links
to SBOL documents, rather than annotating SBOL documents with links to external objects.)

In practice,
embedding large amounts of non-SBOL data into SBOL documents is likely
to cause problems for people and software tools trying to manage and
exchange such documents.  Therefore, it is RECOMMENDED that small amounts of information (e.g., design notes or preferred graphical layout) be embedded in the SBOL model, while large amounts of information (e.g., the contents of the scientific publication from which a model was derived or flow cytometry data that characterizes performance) be linked with IRIs pointing to external resources.  The boundary between "small" and "large" is left deliberately vague, recognizing that it will likely depend on the particulars of a given SBOL application.
