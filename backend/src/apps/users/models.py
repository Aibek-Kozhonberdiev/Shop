from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from ..base.services import FileSizeValidator, path_avatar_user, validation_phone
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, error_messages={'unique': _("Пользователь с таким адресом электронной почты уже существует.")})
    phone = models.CharField(
        max_length=16, verbose_name='Телефонный номер',
        help_text='Введите телефонный номер в международном формате (+996)',
        validators=[validation_phone], unique=True,
        error_messages={'unique': _("Пользователь с таким номером телефона уже существует.")}
    )
    avatar = models.ImageField(
        null=True, blank=True, upload_to=path_avatar_user, verbose_name='Изображение пользователя',
        help_text='Загрузите изображение пользователя',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), FileSizeValidator(max_size_mb=0.5)]
    )
    email_confirmed = models.BooleanField(default=False, blank=True)
    phone_confirmed = models.BooleanField(default=False, blank=True)
    key = models.BinaryField(null=True, blank=True)
    key_valid = models.BooleanField(default=False)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['email', 'phone']

    class Meta:
        app_label = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
