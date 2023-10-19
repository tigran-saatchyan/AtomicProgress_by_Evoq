import json

from django_celery_beat.models import CrontabSchedule, PeriodicTask

from habits.models import Habit


def schedule_notification(habit: Habit, telegram_user_id):
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=habit.time_to_behave.minute,
        hour=habit.time_to_behave.hour,
        day_of_month=f'*/{habit.period_days}'
    )

    task = PeriodicTask.objects.filter(
        name=f'Notification for Telegram user with ID: {telegram_user_id}'
    ).first()
    if task:
        task.crontab = schedule
        task.save()
    else:
        PeriodicTask.objects.create(
            crontab=schedule,
            name=f'Notification for Telegram user with ID: {telegram_user_id}',
            task='habits.tasks.send_notification',
            args=json.dumps([str(habit), telegram_user_id]),
            one_off=False,
        )
