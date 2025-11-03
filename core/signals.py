from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, CallbackRequest
from .tg_bot import send_telegram_message
from django.conf import settings
import asyncio

api_key = settings.TELEGRAM_BOT_API_KEY
user_id = settings.TELEGRAM_USER_ID

def send_telegram_notification(instance):
    try:
        # Формируем сообщение для Telegram
        tg_markdown_message = f"""
🏠 *Новый заказ натяжных потолков!* 🏠

📏 **Площадь потолка:** {instance.area} м²
🔳 **Количество углов:** {instance.corners} шт.
💡 **Светильники:** {instance.lights} шт.
🔧 **Трубы:** {instance.pipes} шт.
🏗️ **Тип потолка:** {instance.ceiling_type}

📞 **Телефон клиента:** {instance.phone}

💬 **Комментарий:** {instance.comment if instance.comment else "Нет комментария"}

⏰ **Дата заказа:** {instance.created_at.strftime("%d.%m.%Y %H:%M")}
        """

        # Отправляем сообщение в Telegram
        asyncio.run(send_telegram_message(api_key, user_id, tg_markdown_message))
    except Exception as e:
        print(f"Ошибка отправки сообщения в Telegram: {e}")

def send_callback_telegram_notification(instance):
    try:
        # Формируем сообщение для Telegram
        tg_markdown_message = f"""
📞 *Новый запрос обратного звонка!* 📞

📱 **Телефон клиента:** {instance.phone}

⏰ **Дата запроса:** {instance.created_at.strftime("%d.%m.%Y %H:%M")}

💬 *Необходимо перезвонить клиенту!*
        """

        # Отправляем сообщение в Telegram
        asyncio.run(send_telegram_message(api_key, user_id, tg_markdown_message))
    except Exception as e:
        print(f"Ошибка отправки сообщения в Telegram: {e}")

@receiver(post_save, sender=Order)
def notify_telegram_on_order_created(sender, instance, created, **kwargs):
    if created:
        print(f"Создан новый заказ #{instance.id}, отправляем уведомление в Telegram...")
        send_telegram_notification(instance)

@receiver(post_save, sender=CallbackRequest)
def notify_telegram_on_callback_created(sender, instance, created, **kwargs):
    if created:
        print(f"Создан новый запрос обратного звонка #{instance.id}, отправляем уведомление в Telegram...")
        send_callback_telegram_notification(instance)
