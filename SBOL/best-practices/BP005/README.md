# BP 005 -- Completeness and Validation

RDF documents containing serialized SBOL objects might or might not be
entirely self-contained.  A SBOL document is self-contained or "complete" if every SBOL object referred to in the document is contained in the document.  It is RECOMMENDED that serializations be complete whenever practical.  In order words, when serializing an SBOL object, serialize all of the other objects that it points to, then serialize all of the other objects that these objects point to, etc., until the document is complete.

It is important to note that there is no guarantee that an RDF document
contains valid SBOL. When SBOL objects are read from an RDF document,
 the program doing so SHOULD verify that all of the property
values encoded therein have the correct data type (e.g., that the object
pointed to by the *Sequence* property of a
*Component* is really a *Sequence*).
For complete files, this validation can be carried out entirely locally. For files that are not complete, an implementation either needs to have a means of validating those external references (e.g., by
retrieving them from a repository), or it needs to mark them as
unverified and not depend on their correctness.
