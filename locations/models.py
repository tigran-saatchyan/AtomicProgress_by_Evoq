from django.conf import settings
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='location',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
