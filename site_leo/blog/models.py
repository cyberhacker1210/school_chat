from django.db import models


class Planning(models.Model):
    heure = models.CharField(max_length = 20)
    jour = models.CharField(max_length =20)
    matiere = models.CharField(max_length =20, null=True)
    semaine = models.CharField(max_length =20, null=True)


class Classe(models.Model):
    name = models.CharField(max_length = 20)
    # planning = models.ForeignKey(planning)
    planning = models.ForeignKey(Planning, on_delete = models.DO_NOTHING)

