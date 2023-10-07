from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from common.constants import NULLABLE
from locations.models import Location


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='habit',
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        Location,
        related_name='habit',
        on_delete=models.CASCADE
    )
    time_to_behave = models.TimeField(**NULLABLE)
    behavior = models.CharField(max_length=255)
    is_satisfying = models.BooleanField(default=False)
    is_good = models.BooleanField(default=False)
    connected_habit = models.ForeignKey(
        'self',
        **NULLABLE,
        on_delete=models.SET_NULL,
        related_name='habit',
        limit_choices_to={'is_satisfying': True, 'user': user}
    )
    period_days = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(
                1,
                message="Значение должно быть положительным."
            ),
            MaxValueValidator(
                7,
                message="Нельзя выполнять привычку реже, чем 1 раз в 7 дней."
            )
        ]
    )
    reward = models.CharField(max_length=255)
    time_to_complete = models.IntegerField(
        default=120,
        validators=[
            MinValueValidator(
                1,
                message="Значение должно быть положительным."
            ),
            MaxValueValidator(
                120,
                message="Значение не должно превышать 120 секунд."
            )
        ]
    )
    is_public = models.BooleanField(default=False)

    def clean(self):
        if self.is_satisfying and (self.reward or self.connected_habit):
            raise ValidationError(
                "Приятная привычка не может иметь вознаграждения или "
                "связанной привычки."
            )
        if self.connected_habit and self.reward:
            raise ValidationError(
                "Нельзя одновременно указывать связанную привычку и "
                "вознаграждение."
            )

    def __str__(self):
        return (
            f'I will {self.behavior} at {self.time_to_behave} '
            f'in {self.location}'
        )

    class Meta:
        unique_together = [['user', 'connected_habit']]
