from django.urls import path

from locations.apps import LocationsConfig
from locations.views import (
    LocationsRetrieveView, LocationsCreateView,
    LocationsUpdateView, LocationsDestroyView,
)

app_name = LocationsConfig.name

urlpatterns = [
    path('create/', LocationsCreateView.as_view(), name='location-create'),
    path(
        '<int:pk>/', LocationsRetrieveView.as_view(), name='location-retrieve'
    ),
    path(
        'update/<int:pk>/',
        LocationsUpdateView.as_view(),
        name='location-update'
    ),
    path(
        'delete/<int:pk>/',
        LocationsDestroyView.as_view(),
        name='location-destroy'
    )
]
