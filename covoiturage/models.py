from django.contrib.auth import validators
from django.db import models  # noqa: F401

class Trajet(models.Model):
    conducteur = models.CharField(max_length=255)
    ville_depart = models.CharField(max_length=255)
    ville_arrivee = models.CharField(max_length=255)
    heure_depart = models.TimeField()
    places = models.PositiveIntegerField() 
    prix_par_place = models.IntegerField()
    date_depart = models.DateField(null=True)

    class Meta:
        verbose_name = "trajet"
        verbose_name_plural = 'trajets'

        constraints = [
            models.CheckConstraint(
                condition=models.Q(places__gte=1),
                name='places_greater_than_zero'
            )
        ]

    def __str__(self):
        return f"{self.ville_depart} -> {self.ville_arrivee} {self.date_depart} à {self.heure_depart}"


class Reservation(models.Model):
        trajet = models.ForeignKey(
             Trajet,on_delete=models.PROTECT,related_name="reservations"
        )
        nom_passager = models.CharField(max_length=255)
        nombre_place = models.PositiveIntegerField()

        class Meta:
            verbose_name = "reservation"
            verbose_name_plural = 'reservations'