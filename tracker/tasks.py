from celery import shared_task

from users.models import CustomUser

from .services import send_telegram_message


@shared_task
def send_tg_notification(user_id):
    user = CustomUser.objects.get(pk=user_id)
    if user.tg_chat_id:
        message = "Вы создали новую привычку!"
        send_telegram_message(user.tg_chat_id, message)
