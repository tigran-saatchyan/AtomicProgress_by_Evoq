from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.serializers import HabitsSerializer
from habits.services import schedule_notification


class HabitsListView(generics.ListAPIView):
    pagination_class = HabitsPaginator
    serializer_class = HabitsSerializer

    def get_queryset(self):
        return Habit.objects.filter(owner_id=self.request.user.pk)


class HabitsPublicListView(generics.ListAPIView):
    pagination_class = HabitsPaginator
    serializer_class = HabitsSerializer

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitsCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

        habit = serializer.instance
        telegram_user_id = self.request.user.telegram_user_id
        if telegram_user_id is not None:
            schedule_notification(habit, telegram_user_id)
        else:
            return Response(
                {
                    "message": "Please update your profile "
                               "data and add telegram_user_id"
                },
                status.HTTP_400_BAD_REQUEST
            )


class HabitsRetrieveView(generics.RetrieveAPIView):
    serializer_class = HabitsSerializer

    def get_queryset(self):
        return Habit.objects.filter(owner_id=self.request.user.pk)


class HabitsUpdateView(generics.UpdateAPIView):
    serializer_class = HabitsSerializer

    def get_queryset(self):
        return Habit.objects.filter(owner_id=self.request.user.pk)


class HabitsDestroyView(generics.DestroyAPIView):
    serializer_class = HabitsSerializer

    def get_queryset(self):
        return Habit.objects.filter(owner_id=self.request.user.pk)
