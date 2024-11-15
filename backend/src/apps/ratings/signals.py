from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from ..shops.models import Shop
from ..products.models import Product
from .models import RatingShop, RatingProduct


def update_rating(model_instance, related_model, rating_field):
    ratings = related_model.objects.filter(**{rating_field: model_instance})
    total = sum(item.number_rating for item in ratings)
    count = ratings.count()

    rating_value = total / count if count > 0 else 0.0

    if isinstance(model_instance, Product):
        model_instance.product_rating = rating_value
    elif isinstance(model_instance, Shop):
        model_instance.product_rating = rating_value

    model_instance.save()


@receiver(post_delete, sender=RatingProduct)
@receiver(post_save, sender=RatingProduct)
def create_update_rating_of_product(sender, instance, *args, **kwargs):
    update_rating(instance.product, RatingProduct, 'product')


@receiver(post_delete, sender=RatingShop)
@receiver(post_save, sender=RatingShop)
def create_update_rating_of_shop(sender, instance, *args, **kwargs):
    update_rating(instance.shop, RatingProduct, 'shop')
