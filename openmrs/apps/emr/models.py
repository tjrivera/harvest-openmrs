from django.db import models


class Patient(models.Model):
    gender = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)
    birthdate_estimated = models.NullBooleanField('birthdate estimated?', blank=True)

    class Meta(object):
        db_table = u'patient'


class Encounter(models.Model):
    patient = models.ForeignKey(Patient)
    encounter_datetime = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta(object):
        db_table = u'encounter'


class CBCResult(models.Model):
    encounter = models.ForeignKey(Encounter)
    hgb = models.FloatField('hemoglobin (HGB)', null=True)
    wbc = models.FloatField('white blood cells (WBC)', null=True)
    rbc = models.FloatField('red blood cells (RBC)', null=True)
    platelets = models.FloatField(null=True)
    mcv = models.FloatField('mean corpuscular volume (MCV)', null=True)
    hct = models.FloatField('hematocrit', null=True)
    rdw = models.FloatField('red cell distribution width (RDW)', null=True)
    mchc = models.FloatField('mean cell hemoglobin concentration (MCHC)', null=True)
    mch = models.FloatField('mean corpuscular hemoglobin (MCH)', null=True)

    class Meta(object):
        db_table = u'cbc_result'
        verbose_name = 'CBC result'
