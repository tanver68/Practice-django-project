from django.db import models


class Doctor(models.Model):
    id = models.FloatField(blank=True, null=True, primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    age = models.CharField(max_length=30, blank=True, null=True)
    designation = models.CharField(max_length=40, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class Patient(models.Model):
    id = models.CharField(max_length=20, blank=True, null=True, primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    age = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class Physp(models.Model):
    physp_id = models.CharField(max_length=2, primary_key=True)
    physp = models.CharField(max_length=30, blank=True, null=True)
    physp_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physp'








