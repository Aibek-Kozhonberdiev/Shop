from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext as _

from ..base.services import path_avatar_user
from ..base.validators import validation_phone, validate_file_size_avatar


class CustomUser(AbstractUser):
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _("Пользователь с таким адресом электронной почты уже существует."),
        }
    )
    phone = models.CharField(
        max_length=16,
        verbose_name='Телефонный номер',
        help_text='Введите телефонный номер в международном формате',
        validators=[
            validation_phone
        ],
        unique=True,
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
            validate_file_size_avatar
        ]
    )

    REQUIRED_FIELDS = ['email', 'phone']

    class Meta:
        app_label = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
