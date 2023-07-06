# Examples and Use cases

This file contains examples illustrated using UML diagrams.

### Composite Part 

Figure 1 and Figure 2 illustrate two ways of representing the composite part BBa_K093005, one with `Locations` and one with `Constraints`. BBa_K093005 is a product of assembling the RBS BBa_B0034 and CDS BBa_E1010 in accordance with the BioBrick RFC10 standard. A scar is formed between the parts as a result of their assembly. 

![composite_part](images/composite_part_example_1.png "Composite part example UML diagram with Locations")

**Figure 1:** Composite part example UML diagram with `Locations`. 

![composite_part](images/composite_part_example_2.png "Composite part example UML diagram with Locations")

**Figure 2:** Composite part example UML diagram with `Constraints`.

### Backbone 

Figure 3 and Figure 4 illustrate two ways of representing the plasmid vector pSB1C3, one with `Locations` and one with `Constraints`. pSB1C3 includes the prefix and suffix of the BioBrick RFC 10 assembly standard (BBa_G00000 and BBa_G00001, respectively) and an insertion site between these flanking sequences. 

![backbone_1](images/backbone_example_1.png "Backbone example UML diagram with flanking sequences and Locations")

**Figure 3:** Backbone example UML diagram with flanking sequences and `Locations`. The contents of BBa_G00000 are purposefully omitted for simplicity of presentation.

![backbone_2](images/backbone_example_2.png "Backbone example UML diagram with flanking sequences and Constraints")

**Figure 4:** Backbone example UML diagram with flanking sequences and `Constraints`. The contents of BBa_G00000 are purposefully omitted for simplicity of presentation.

### Part in Backbone 

Figures 5, 6, 7, and 8 illustrate different ways of representing the plasmid vector pSB1C3 with a BBa_E1010 insert. Figure 5 and Figure 6 show how to represent BBa_E1010 in pSB1C3 with `Locations` and `Constraints`, respectively.

![part_in_backbone_1](images/part_in_backbone_example_1.png "Part in backbone example UML diagram with flanking sequences in backbone and Locations")

**Figure 5:** Part in backbone example UML diagram with flanking sequences in backbone and `Locations`. The contents of BBa_G00000 and BBa_G00001 are purposefully omitted for simplicity of presentation.

![part_in_backbone_2](images/part_in_backbone_example_2.png "Part in backbone example UML diagram with flanking sequences in backbone and Constraints")

**Figure 6:** Part in backbone example UML diagram with flanking sequences in backbone and `Constraints`. The contents of BBa_G00000 and BBa_G00001 are purposefully omitted for simplicity of presentation.

![part_in_backbone_3](images/part_in_backbone_example_3.png "Part in backbone example UML diagram with flanking sequences in part insert and Locations")

By contrast, Figure 7 and Figure 8 show two ways to represent the assembly flanking sequences as part of the BBa_E101 insert instead of the pSB1C3 backbone. In Figure 7, these flanking sequences are the BioBrick RFC 10 prefix and suffix, but in Figure 8 they are overhangs resulting from cleaving the prefix and suffix with the restriction enzymes XbaI and PstI. Note that these overhangs are still contained by the RFC 10 prefix and suffix in the context of the overall "part in backbone" representation in Figure 8.

**Figure 7:** Part in backbone example UML diagram with flanking sequences in part insert and `Locations`. The contents of BBa_G00000 and BBa_G00001 are purposefully omitted for simplicity of presentation.

![part_in_backbone_4](images/part_in_backbone_example_4.png "Part in backbone example UML diagram with flanking sequences in part insert/extract and Locations")

**Figure 8:** Part in backbone example UML diagram with flanking sequences in part insert/extract and `Locations`. The contents of BBa_G00000 and BBa_G00001 are purposefully omitted for simplicity of presentation.

### Part Extract 

Figure 9 and Figure 10 illustrate two ways of representing the result of extracting a BBa_E1010 insert from pSB1C3, one with `Locations` and one with `Constraints`. Extraction was done using the XbaI and PstI restriction enzymes.

![part_extract_1](images/part_extract_example_1.png "Part extract example UML diagram with Locations")

**Figure 9:** Part extract example UML diagram with `Locations`.

![part_extract_2](images/part_extract_example_2.png "Part extract example UML diagram with Constraints")

**Figure 10:** Part extract example UML diagram with `Constraints`.

### Assembly 

Figure 11 illustrates one way of representing the assembly of BBa_B0034 and BBa_E1010 into BBa_K093005 in accordance with the BioBrick RFC10 standard. Extraction of BBa_B0034 its part in backbone is represented with the EcoRI and SpeI restriction enzymes as participants, while extraction of BBa_E1010 is represented with the XbaI and PstI restriction enzymes as participants. The resulting part extracts with the appropriate overhangs are then represented as participants in their ligation into BBa_K093005. The positions of features within all parts and backbones are specified using `Locations`, and parts in backbones are represented with the flanking sequences for assembly placed in the pSB1C3 backbone as opposed to their engineering inserts.

![assembly](images/assembly_example.png "Assembly example UML diagram with flanking sequences in backbone and Locations")

**Figure 11:** Assembly example UML diagram with flanking sequences in backbone and `Locations`. The contents of BBa_G00000 and BBa_G00001 are purposefully omitted for simplicity of presentation. Objects are color-coded based on what they represent: orange is for the assembly plan, blue is for backbone, green is for part in backbone, yellow is for composite part, and pink is for part extract.
