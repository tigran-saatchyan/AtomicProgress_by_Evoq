from rest_framework import generics

from locations.models import Location
from locations.serializers import LocationsSerializer


class LocationsCreateView(generics.CreateAPIView):
    serializer_class = LocationsSerializer

    def get_queryset(self):
        return Location.objects.filter(user_id=self.request.user.pk)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LocationsRetrieveView(generics.RetrieveAPIView):
    serializer_class = LocationsSerializer

    def get_queryset(self):
        return Location.objects.filter(user_id=self.request.user.pk)


class LocationsUpdateView(generics.UpdateAPIView):
    serializer_class = LocationsSerializer

    def get_queryset(self):
        return Location.objects.filter(user_id=self.request.user.pk)


class LocationsDestroyView(generics.DestroyAPIView):
    serializer_class = LocationsSerializer

    def get_queryset(self):
        return Location.objects.filter(user_id=self.request.user.pk)
