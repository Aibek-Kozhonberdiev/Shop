from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

from ..base.services import path_avatar_user
from ..base.validators import validation_phone, validate_file_size_avatar


class CustomUser(AbstractUser):
    phone = models.CharField(
        max_length=16,
        verbose_name='Телефонный номер',
        help_text='Введите телефонный номер в международном формате',
        validators=[
            validation_phone,
            validate_file_size_avatar
        ]
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to=path_avatar_user,
        verbose_name='Изображение пользователя',
        help_text='Загрузите изображение пользователя',
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'jpg',
                    'png',
                ]
            ),

        ]
    )

    class Meta:
        app_label = 'users'
