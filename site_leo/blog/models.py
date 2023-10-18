from django.db import models


class Planning(models.Model):
    heure = models.CharField(max_length = 20)
    jour = models.CharField(max_length =20)
    matiere = models.CharField(max_length =20, null=True)
    semaine = models.CharField(max_length =20, null=True)
    groupe = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.jour} - {self.heure} - {self.groupe}'


class Classe(models.Model):
    name = models.CharField(max_length = 20)
    planning = models.ForeignKey(Planning, on_delete = models.DO_NOTHING)

