from django.shortcuts import get_object_or_404, redirect, render  # noqa: F401
from .models import Trajet,Reservation
from django.utils import timezone

def liste_trajets(request):
    trajets = Trajet.objects.filter(date_depart__gte=timezone.now().date())
    return render(
        request,
        "covoiturage/list_trajets.html",
        {"trajets":trajets}
    )
