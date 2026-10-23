from django.urls import path  # noqa: F401

from . import views  # noqa: F401

app_name = "covoiturage"

urlpatterns = [
    path("trajet/index",view= views.liste_trajets,
        name="list_trajets")
]
