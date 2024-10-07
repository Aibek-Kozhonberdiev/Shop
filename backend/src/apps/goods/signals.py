from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Product, ProductRating


@receiver(post_delete, sender=ProductRating)
@receiver(post_save, sender=ProductRating)
def create_update_rating_of_shop(sender, instance, *args, **kwargs):
    ratings = ProductRating.objects.filter(product=instance.product)
    total = 0
    count = 0
    for item in ratings:
        total += item.number_rating
        count += 1
    shop = Product.objects.get(pk=instance.shop_id)
    shop.product_rating = total / count if not total == 0 else 0.0
    shop.save()
