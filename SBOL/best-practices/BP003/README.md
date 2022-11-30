# BP 003 -- Versioning SBOL Objects

SBOL 3.x does not specify an explicit versioning scheme. Rather it is left for experimentation across different tools. This allows version information to be included in the root (e.g., GitHub style: "igem/HEAD/"), collection structure (e.g., "promoters/constitutive/2/), in tool-specific conventions on `displayId` (e.g., "BBa\_J23101\_v2) or in information outside of the *IRI* (e.g., by attaching `prov:wasRevisionOf` properties).
