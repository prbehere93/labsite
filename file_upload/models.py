from django.db import models
from django.db.models.deletion import PROTECT
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _ #for making textchoices



# Create your models here.
class Document(TimeStampedModel):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/') #is uploaded to media_root/documents
    
class trait(TimeStampedModel):
    trait_id=models.CharField(max_length=50, unique=True)
    trait_name=models.CharField(max_length=50)
    method_id=models.CharField(max_length=50)
    method_name=models.CharField(max_length=50)
    method_description=models.CharField(max_length=50)
    scale_id=models.CharField(max_length=50)
    scale_name=models.CharField(max_length=50)
    scale_ll=models.CharField(max_length=50)
    scale_ul=models.CharField(max_length=50)
    method_ref=models.CharField(max_length=50)


class meta_trait(TimeStampedModel):
    meta_trait_id=models.CharField(max_length=50, unique=True)
    name=models.CharField(max_length=50)
    traits=models.ForeignKey(trait, on_delete=models.PROTECT) #one to many relationship here (can link multiple traits to a single meta_trait_id)

class observation(TimeStampedModel):
    accession=models.CharField(max_length=50)
    trait=models.CharField(max_length=50)
    biological_replicate=models.CharField(max_length=4)
    technical_replicate=models.CharField(max_length=4)
    value=models.DecimalField(max_digits=1000,decimal_places=4,null=True,blank=True)

class study(TimeStampedModel):

    class GrowthFacilityType(models.TextChoices):
        FIELD = 'field', _('Field')
        GREENHOUSE= 'greenhouse',_('Green House')
        CULTURE_ROOM='culture_room',_('Culture Room')
        PHYTOTRON='phytotron',_('Phytotron')

    class TreatmentType(models.TextChoices):
        BIOTIC = 'biotic', _('Biotic')
        ABIOTIC = 'abiotic', _('Abiotic')
        OTHER= 'other', _('Other')

    class DataType(models.TextChoices):
        PHENOTYPIC = 'phenotypic', _('Phenotype')
        GENOTYPIC = 'genotypic', _('Genotypic')

    study_id=models.CharField(max_length=100,unique=True) #will also contain a callable function that will be used to autogenerate this id (use JS)
    user=models.ForeignKey(User, on_delete=PROTECT) #will probably be Profile here(in the RLR website)
    meta_trait=models.CharField(max_length=50,blank=False,null=False) #should be a FK
    meta_trait_id=models.ForeignKey(meta_trait, on_delete=PROTECT)
    title=models.CharField(max_length=100,blank=True,null=True)
    description=models.CharField(max_length=200, blank=True, null=True)
    start_date=models.DateField(blank=True, null=True)
    end_date=models.DateField(blank=True, null=True) #add conditions to check if end_date is > start_date
    location=models.CharField(max_length=50,blank=True, null=True)
    description_experimental_design=models.CharField(max_length=500,blank=False,null=False)
    growth_facility=models.CharField(max_length=20, choices=GrowthFacilityType.choices, blank=True, null=True)
    temperature=models.DecimalField(max_digits=6,decimal_places=3) # can store 100.998
    light_intensity=models.DecimalField(max_digits=6,decimal_places=3)
    relative_humidity=models.DecimalField(max_digits=6,decimal_places=3) #add a condition to limit this between 0.000 and 100.000
    other_conditions=models.CharField(max_length=100)
    treatment_type=models.CharField(max_length=10, choices=TreatmentType.choices, blank=True, null=True) #biotic/abiotic/other
    treatment_description=models.CharField(max_length=150, blank=True, null=True)
    treatment_name=models.CharField(max_length=50)
    treatment_value=models.CharField(max_length=50)
    treatment_developmental_stage=models.CharField(max_length=50)
    data_type=models.CharField(max_length=20,choices=DataType.choices,default=DataType.PHENOTYPIC)
    observation_developmental_stage=models.CharField(max_length=100, blank=True, null=True)
    tissue=models.CharField(max_length=100) #should be a foreign field linked to ontology
    biological_replicates=models.IntegerField()
    technical_replicates=models.IntegerField()
    trait_name=models.CharField(max_length=100)
    observation=models.ForeignKey(observation)