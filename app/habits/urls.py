from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitsListView, HabitsPublicListView, HabitsCreateView,
    HabitsRetrieveView, HabitsUpdateView, HabitsDestroyView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitsListView.as_view(), name='habits-list'),
    path('public/', HabitsPublicListView.as_view(), name='habits-public-list'),
    path('create/', HabitsCreateView.as_view(), name='habit-create'),
    path('<int:pk>/', HabitsRetrieveView.as_view(), name='habit-retrieve'),
    path('update/<int:pk>/', HabitsUpdateView.as_view(), name='habit-update'),
    path('delete/<int:pk>/', HabitsDestroyView.as_view(), name='habit-destroy')

]
