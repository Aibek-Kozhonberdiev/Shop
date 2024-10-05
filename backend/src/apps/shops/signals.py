from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Shop, Complaint, Rating


User = get_user_model()


@receiver(post_save, sender=Complaint)
def create_complaint_of_shop(sender, instance, created, **kwargs):
    if created:
        shop = Shop.objects.get(pk=instance.shop_id)
        shop.number_of_complaints += 1
        shop.save()


@receiver(post_delete, sender=Complaint)
def delite_complaint_of_shop(sender, instance, **kwargs):
    shop = Shop.objects.get(pk=instance.shop_id)
    if shop.number_of_complaints > 0:
        shop.number_of_complaints -= 1
        shop.save()


@receiver(post_delete, sender=Rating)
@receiver(post_save, sender=Rating)
def create_update_rating_of_shop(sender, instance, *args, **kwargs):
    ratings = Rating.objects.filter(shop=instance.shop)
    total = 0
    count = 0
    for item in ratings:
        total += item.number_rating
        count += 1
    shop = Shop.objects.get(pk=instance.shop_id)
    shop.average_rating = total / count if not total == 0 else 0.0
    shop.save()
