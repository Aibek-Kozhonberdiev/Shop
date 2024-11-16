from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import Complain
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
