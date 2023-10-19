from django.test import TestCase

from locations.models import Location
from users.models import User


class LocationTest(TestCase):

    LOCATION_NAME = 'Sample Place'

    def setUp(self):
        self.user = User.objects.create(
            email='user@test.test', password='test'
        )
        self.location = Location.objects.create(
            name=self.LOCATION_NAME,
            user=self.user
        )

    def test_add_read_locations(self):
        self.assertEqual(self.location.name, self.LOCATION_NAME)
        self.assertEqual(self.location.user, self.user)
