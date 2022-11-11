# BP 001 -- SBOL Versions

To differentiate between major versions of SBOL, different namespaces are used.  For example, SBOL3 has the namespace http://sbols.org/v3#, while SBOL2 has the namespace http://sbols.org/v2#.  These different versions of SBOL SHOULD NOT be semantically mixed. For example, an SBOL 3.x *SubComponent* SHOULD NOT refer to an SBOL 2.x **ComponentInstance**, and, likewise, an SBOL 2.x **ComponentInstance** SHOULD NOT refer to an SBOL 1.x **DnaComponent**.
