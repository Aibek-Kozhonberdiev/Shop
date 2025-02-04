from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Chat, Message


@receiver(post_save, sender=Chat)
@receiver(post_delete, sender=Chat)
def send_notification_chat_user(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    users = instance.users
    for user in users:
        async_to_sync(channel_layer.group_send)(
            f"user_{user.id}",
            {
                'type': 'order_status',
                'status': instance.status,
                'order_id': instance.id,
            },
        )


@receiver(post_save, sender=Message)
@receiver(post_delete, sender=Message)
def send_notification_message_user(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    chat = Chat.objects.get(pk=instance.chat)
    for user in chat.users:
        async_to_sync(channel_layer.group_send)(
            f"user_{user.id}",
            {
                'type': 'order_status',
                'status': instance.status,
                'order_id': instance.id,
            },
        )
