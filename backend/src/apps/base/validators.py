from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validation_phone(value):
    if value[0:3] != "+996":
        raise ValidationError(
            _("Номер не соответствует кодировке Кыргызстана"),
            params={"value": value},
        )


def validate_file_size_avatar(file):
    max_size_kb = 1024 # 1 MB in KB
    if file.size > max_size_kb:
        raise ValidationError(f"Размер файла не должен превышать {max_size_kb / 1000} MB")
