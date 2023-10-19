from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from users.models import User


@shared_task
def activity_check():
    due_date = timezone.now() - timedelta(days=30)
    queryset = User.objects.filter(last_login__lte=due_date)
    queryset.update(is_active=False)


@shared_task
def send_notification(recipient_email, message, subject):
    send_mail(
        subject=subject,
        message=message,
        from_email=None,
        recipient_list=[recipient_email],
        html_message=message,
    )
