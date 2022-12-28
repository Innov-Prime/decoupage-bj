from django.db import models
from django.db.models import IntegerField


class Departement(models.Model):
    id_dep = models.IntegerField(null=False)
    lib_dep = models.CharField(max_length=255)


class Commune(models.Model):
    id_com = models.IntegerField(null=False)
    lib_com = models.CharField(max_length=255)
    id_dep = models.IntegerField(null=False)



class Arrondissement(models.Model):
    id_arrond: IntegerField = models.IntegerField(null=False)
    lib_arrond = models.CharField(max_length=255)
    id_com = models.IntegerField(null=False)


class Quartier(models.Model):
    id_quart = models.IntegerField(null=False)
    lib_quart = models.CharField(max_length=255)
    id_arrond = models.IntegerField(null=False)
