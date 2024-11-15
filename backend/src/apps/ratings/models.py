from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from ..shops.models import Shop
from ..products.models import Product


User = get_user_model()

class RatingShop(models.Model):
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    created_to = models.DateTimeField(auto_now_add=True)
    updated_to = models.DateTimeField(auto_now=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'shop')


class RatingProduct(models.Model):
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    created_to = models.DateTimeField(auto_now_add=True)
    updated_to = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'shop')
