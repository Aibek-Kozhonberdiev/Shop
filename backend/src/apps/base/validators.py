from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validation_phone(value):
    if value[0:4] != "+996":
        raise ValidationError(
            _("Номер не соответствует кодировке Кыргызстана"),
            params={"value": value},
        )


def validate_file_size_avatar(file):
    max_size_mb = 3
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Размер файла не должен превышать {max_size_mb}MB")
