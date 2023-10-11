from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.serializers import HabitsSerializer


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
