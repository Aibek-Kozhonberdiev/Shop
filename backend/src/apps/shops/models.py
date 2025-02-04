from decimal import Decimal
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.db import models

from ..base.services import FileSizeValidator, path_logo_shop, path_background_shop


User = get_user_model()

class Shop(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1500)
    logo = models.ImageField(
        upload_to=path_logo_shop,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'png']),
            FileSizeValidator(max_size_mb=3)
        ]
    )
    background = models.ImageField(
        upload_to=path_background_shop,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'png']),
            FileSizeValidator(max_size_mb=3)
        ]
    )
    address = models.URLField()
    indicate_address = models.BooleanField(default=True, blank=True)
    number_of_complaints = models.PositiveIntegerField(default=0, blank=True)
    link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(
        default=Decimal('0.00'), max_digits=3, decimal_places=2,
        validators=[
            MaxValueValidator(5.0),
            MinValueValidator(1.0)
        ]
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
