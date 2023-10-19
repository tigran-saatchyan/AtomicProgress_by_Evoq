from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from habits.models import Habit
from locations.models import Location
from users.models import User


class HabitsViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='testuser@test.test',
            password='testpassword',
        )

        self.location_data = {
            "name": "testlocation",
            "user": self.user
        }

        self.location = Location.objects.create(
            **self.location_data
        )

        self.habit_data = {
            "location": self.location,
            "time_to_behave": "00:00",
            "behavior": "be happy",
            "is_satisfying": True,
            "reward": None,
            "connected_habit": None,
            "period_days": 1,
            "time_to_complete": 60,
            "is_good": False,
            "is_public": False,
            "owner": self.user
        }
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            **self.habit_data
        )
        self.habit_data.update(
            {
                "location": self.location.name,
                "owner": self.user.id
            }
        )
        self.url_list = reverse('habits:habits-list')
        self.url_public_list = reverse('habits:habits-public-list')
        self.url_create = reverse('habits:habit-create')
        self.url_retrieve = reverse(
            'habits:habit-retrieve',
            args=[self.habit.pk]
        )
        self.url_update = reverse(
            'habits:habit-update',
            args=[self.habit.pk]
        )
        self.url_destroy = reverse(
            'habits:habit-destroy',
            args=[self.habit.pk]
        )

    def test_habits_list_view(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habits_public_list_view(self):
        response = self.client.get(self.url_public_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habits_create_view(self):
        self.client.force_authenticate(user=self.user)

        habit_data = self.habit_data

        habit_data.update(
            {
                "location": self.location.name,
                "owner": self.user.id
            }
        )

        response = self.client.post(
            self.url_create, habit_data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habits_retrieve_view(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_retrieve)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habits_update_view(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'behavior': 'Updated Habit Name'
        }
        response = self.client.patch(
            self.url_update, data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habits_destroy_view(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.url_destroy)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_simultaneous_connected_habit_and_reward_constrain(self):
        self.client.force_authenticate(user=self.user)
        habit_data = self.habit_data
        habit_data.update(
            {
                "reward": "testreward",
                "connected_habit": self.habit.pk,
                "is_satisfying": False,
                "location": self.location.name,
                "owner": self.user.id
            }
        )

        expected_message = (
            "Нельзя одновременно указывать связанную привычку и "
            "вознаграждение."
        )
        with self.assertRaisesMessage(ValidationError, expected_message):
            response = self.client.post(
                self.url_create, habit_data, format='json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_time_to_complete_min(self):
        self.client.force_authenticate(user=self.user)
        habit_data = self.habit_data
        habit_data.update(
            {
                "time_to_complete": -1,
                "location": self.location.name,
                "owner": self.user.id

            }
        )

        response = self.client.post(
            self.url_create, habit_data, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_time_to_complete_max(self):
        self.client.force_authenticate(user=self.user)

        habit_data = self.habit_data
        habit_data.update(
            {
                "time_to_complete": 500,
                "location": self.location.name,
                "owner": self.user.id
            }
        )

        response = self.client.post(
            self.url_create, habit_data, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_connected_habit_to_be_satisfying(self):
        self.client.force_authenticate(user=self.user)

        habit_data = self.habit_data
        self.habit.is_satisfying = False
        self.habit.save()
        habit_data.update(
            {
                "connected_habit": self.habit.pk,
                "location": self.location.name,
                "owner": self.user.id
            }
        )

        response = self.client.post(
            self.url_create, habit_data, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_satisfying_habit_have_no_connected_habit(self):
        self.client.force_authenticate(user=self.user)

        habit_data = self.habit_data
        habit_data.update(
            {
                "connected_habit": self.habit.pk,
                "location": self.location.name,
                "owner": self.user.id
            }
        )

        expected_message = (
            "Приятная привычка не может иметь вознаграждения или "
            "связанной привычки."
        )
        with self.assertRaisesMessage(ValidationError, expected_message):
            response = self.client.post(
                self.url_create, habit_data, format='json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_satisfying_habit_have_no_reward(self):
        self.client.force_authenticate(user=self.user)

        habit_data = self.habit_data
        habit_data.update(
            {
                "reward": "testreward",
                "location": self.location.name,
                "owner": self.user.id
            }
        )

        expected_message = (
            "Приятная привычка не может иметь вознаграждения или "
            "связанной привычки."
        )
        with self.assertRaisesMessage(ValidationError, expected_message):
            response = self.client.post(
                self.url_create, habit_data, format='json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_habit_completion_period(self):
        self.client.force_authenticate(user=self.user)

        habit_data = self.habit_data
        habit_data.update(
            {
                "period_days": 8,
                "location": self.location.name,
                "owner": self.user.id
            }
        )

        response = self.client.post(
            self.url_create, habit_data, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
