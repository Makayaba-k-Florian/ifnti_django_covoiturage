from django.db import models  # noqa: F401

class Trajet(models.Model):
    conducteur = models.CharField(max_length=255)
    ville_depart = models.CharField(max_length=255)
    ville_arrivee = models.CharField(max_length=255)
    heure_depart = models.TimeField()
    places = models.PositiveIntegerField() 
    prix_par_place = models.IntegerField()

    class Meta:
        verbose_name = "trajet"
        verbose_name_plural = 'trajets'

