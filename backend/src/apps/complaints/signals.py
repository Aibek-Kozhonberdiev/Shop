from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import Complain, Support


def send_status_admin(instance):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "admin",
        {
            'type': 'order_status',
            'status': instance.status,
            'order_id': instance.id,
        },
    )


@receiver(post_delete, sender=Complain)
@receiver(post_save, sender=Complain)
def add_complain_shop(sender, instance, *args, **kwargs):
    shop = instance.shop
    if sender == post_save:
        shop.number_of_complaints += 1
    else:
        shop.number_of_complaints -= 1

    shop.save()
    send_status_admin(instance)


@receiver(post_save, sender=Support)
@receiver(post_delete, sender=Support)
def send_delete_support_ws(sender, instance, **kwargs):
    send_status_admin(instance)
