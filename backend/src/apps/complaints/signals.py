from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import Complain, Support
from ..shops.models import Shop


@receiver(post_save, sender=Complain)
def add_complain_shop(sender, instance, *args, **kwargs):
    shop = Shop.objects.get(pk=instance.shop)
    shop.number_of_complaints += 1
    shop.save()


@receiver(post_delete, sender=Complain)
def delete_complain_shop(sender, instance, *args, **kwargs):
    shop = Shop.objects.get(pk=instance.shop)
    if not shop.number_of_complaints <= 0:
        shop.number_of_complaints -= 1
    shop.save()


@receiver(post_save, sender=Support)
@receiver(post_delete, sender=Support)
def send_delete_support_ws(sender, instance):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "admin",
        {
            'type': 'order_status',
            'status': instance.status,
            'order_id': instance.id,
            'title': instance.title,
            'user': instance.user
        },
    )
