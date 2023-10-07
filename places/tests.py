from django.test import TestCase

from places.models import Place
from users.models import User


class PlaceTest(TestCase):

    PLACE_NAME = 'Sample Place'

    def setUp(self):
        self.user = User.objects.create(
            email='user@test.test', password='test'
        )
        self.place = Place.objects.create(
            name=self.PLACE_NAME,
            user=self.user
        )

    def test_add_read_place(self):
        self.assertEqual(self.place.name, self.PLACE_NAME)
        self.assertEqual(self.place.user, self.user)
