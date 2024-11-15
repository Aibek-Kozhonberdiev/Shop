from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator
from django.db import models

from ..base.services import FileSizeValidator, path_photo_product


class Product(models.Model):
    title = models.CharField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    currency = models.CharField()
    rating = models.DecimalField(
        max_length=3, decimal_places=2, default=Decimal("0.00"), blank=True,
        validators=[MaxValueValidator(5.0), MinValueValidator(0.0)]
    )
    create_to = models.DateTimeField(auto_now_add=True)
    sab_category = models.ForeignKey("SubCategory", on_delete=models.PROTECT)


class FotoProduct(models.Model):
    foto = models.ImageField(
        upload_to=path_photo_product,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg']), FileSizeValidator(max_size_mb=1)]
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField()
    icon = models.ImageField(
        upload_to='icons/',
        validators=[FileExtensionValidator(allowed_extensions=['png']), FileSizeValidator(max_size_mb=1)]
    )


class SubCategory(models.Model):
    title = models.CharField()
    icon = models.ImageField(
        upload_to='icons/',
        validators=[FileExtensionValidator(allowed_extensions=['png']), FileSizeValidator(max_size_mb=1)]
    )
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
