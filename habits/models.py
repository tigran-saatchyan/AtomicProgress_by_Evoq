from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from common.constants import NULLABLE
from locations.models import Location


class Habit(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='habit',
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        Location,
        related_name='habit',
        on_delete=models.CASCADE
    )
    time_to_behave = models.TimeField()
    behavior = models.CharField(max_length=255)
    is_satisfying = models.BooleanField(default=False)
    is_good = models.BooleanField(default=False)
    connected_habit = models.ForeignKey(
        'Habit',
        **NULLABLE,
        on_delete=models.SET_NULL,
        limit_choices_to={'is_satisfying': True}
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
    reward = models.CharField(max_length=255, **NULLABLE)
    time_to_complete = models.IntegerField(
        default=60,
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
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

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

    def save(self, *args, **kwargs):

        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f'I will {self.behavior} at {self.time_to_behave} '
            f'in {self.location}'
        )
