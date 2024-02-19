from datetime import timedelta

from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task
from celery.utils.log import get_task_logger

from .models import BirthDayRecord


logger = get_task_logger(__name__)


@shared_task
def notify_customers():
    today = timezone.now()
    tomorrow = today + timedelta(days=1)

    birthdays_tomorrow = BirthDayRecord.objects.filter(
        date_of_birth__month=tomorrow.month, date_of_birth__day=tomorrow.day
    )

    for birthday_record in birthdays_tomorrow:
        logger.info(birthday_record.id)
        send_mail(
            "Birthday Reminder!",
            f"Tomorrow {tomorrow.day}/{tomorrow.month}/{tomorrow.year} is {birthday_record.name}'s Birth Day!",
            settings.DEFAULT_FROM_EMAIL,
            [birthday_record.user.email],
        )

    logger.info("Done")
    return True

