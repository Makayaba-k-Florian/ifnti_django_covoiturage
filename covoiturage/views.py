from django.shortcuts import get_object_or_404, redirect, render  # noqa: F401
from .models import Trajet,Reservation


def liste_trajets(request):
    trajets = Trajet.objects.all()
    return render(
        request,
        "covoiturage/list_trajets.html",
        {"trajets":trajets}
    )
