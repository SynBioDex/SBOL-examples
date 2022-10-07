import sbol3
import tyto

doc = sbol3.Document()
sbol3.set_namespace('https://github.com/Gonza10V')

backbone_identity = 'backbone'
backbone_sequence = 'aaGGGGttttCCCCaa'
dropout_location = [3,15]
fusion_site_length = 4
test_description = 'test'

circular_backbone_seq = sbol3.Sequence(f'{backbone_identity}_seq', elements=backbone_sequence, encoding=sbol3.IUPAC_DNA_ENCODING)
circular_backbone_component =  sbol3.Component(backbone_identity, types=[sbol3.SBO_DNA, sbol3.SO_CIRCULAR], roles=[sbol3.SO_DOUBLE_STRANDED, tyto.SO.plasmid_vector], sequences=[circular_backbone_seq], description=test_description)

dropout_location_comp = sbol3.Range(sequence=circular_backbone_seq, start=dropout_location[0], end=dropout_location[1])
insertion_site_location1 = sbol3.Range(sequence=circular_backbone_seq, start=dropout_location[0], end=dropout_location[0]+fusion_site_length, order=1)
insertion_site_location2 = sbol3.Range(sequence=circular_backbone_seq, start=dropout_location[1]-fusion_site_length, end=dropout_location[1], order=3)
open_backbone_location1 = sbol3.Range(sequence=circular_backbone_seq, start=1, end=dropout_location[0]+fusion_site_length -1, order=2)
open_backbone_location2 = sbol3.Range(sequence=circular_backbone_seq, start=dropout_location[1]-fusion_site_length, end=len(backbone_sequence), order=1)
dropout_sequence_feature = sbol3.SequenceFeature(locations=[dropout_location_comp], roles=[tyto.SO.deletion])
insertion_sites_feature = sbol3.SequenceFeature(locations=[insertion_site_location1, insertion_site_location2], roles=[tyto.SO.insertion_site])
open_backbone_feature = sbol3.SequenceFeature(locations=[open_backbone_location1, open_backbone_location2])

circular_backbone_component.features.append(dropout_sequence_feature)
circular_backbone_component.features.append(insertion_sites_feature)
circular_backbone_component.features.append(open_backbone_feature)
backbone_dropout_meets = sbol3.Constraint(restriction='http://sbols.org/v3#meets', subject=dropout_sequence_feature, object=open_backbone_feature)
circular_backbone_component.constraints.append(backbone_dropout_meets)
doc.add([circular_backbone_component, circular_backbone_seq])
doc.write('circular_backbone.nt', sbol3.SORTED_NTRIPLES)