from celery import shared_task

from users.models import CustomUser

from .services import send_telegram_message


@shared_task
def send_tg_notification():
    for user in CustomUser.objects.filter(tg_chat_id__isnull=False):
        if user.tg_chat_id:
            message = "Не забудьте про ежедневную привычку!"
            send_telegram_message(user.tg_chat_id, message)
