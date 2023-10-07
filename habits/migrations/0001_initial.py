# Generated by Django 4.2.6 on 2023-10-07 20:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_to_behave', models.TimeField(blank=True, null=True)),
                ('behavior', models.CharField(max_length=255)),
                ('is_satisfying', models.BooleanField(default=False)),
                ('is_good', models.BooleanField(default=False)),
                ('period_days', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Значение должно быть положительным.'), django.core.validators.MaxValueValidator(7, message='Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')])),
                ('reward', models.CharField(max_length=255)),
                ('time_to_complete', models.IntegerField(default=120, validators=[django.core.validators.MinValueValidator(1, message='Значение должно быть положительным.'), django.core.validators.MaxValueValidator(120, message='Значение не должно превышать 120 секунд.')])),
                ('is_public', models.BooleanField(default=False)),
                ('connected_habit', models.ForeignKey(blank=True, limit_choices_to={'is_satisfying': True, 'user': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habit', to=settings.AUTH_USER_MODEL)}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='habit', to='habits.habit')),
            ],
        ),
    ]
