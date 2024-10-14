from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


def validation_phone(value):
    if value[0:4] != "+996":
        raise ValidationError(
            _("Номер не соответствует кодировке Кыргызстана."),
            params={"value": value},
        )


@deconstructible
class FileSizeValidator:
    message = _(
        "Размер файла не должен превышать %(max_size_mb)MB."
    )

    def __init__(self, max_size_mb=1):
        self.max_size_mb = max_size_mb

    def __call__(self, value):
        if value.size > self.max_size_mb * 1024 * 1024:
            raise ValidationError(self.message)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.max_size_mb == other.max_size_mb
        )
