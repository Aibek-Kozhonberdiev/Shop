from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator

from ..base.services import path_background_shop, path_logo_shop, path_screenshot_complaint
from ..base.validators import validate_foto_base, validate_foto_logo_shop

User = get_user_model()


class Shop(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Название магазина",
        help_text="Введите название магазина (максимум 150 символов)"
    )
    description = models.TextField(
        max_length=350,
        null=True,
        blank=True,
        verbose_name="Описание",
        help_text="Введите краткое описание магазина (максимум 350 символов)"
    )
    logo = models.ImageField(
        upload_to=path_logo_shop,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'jpg',
                    'png',
                ]
            ),
            validate_foto_logo_shop
        ],
        verbose_name="Логотип",
        help_text="Загрузите логотип магазина"
    )
    background = models.ImageField(
        upload_to=path_background_shop,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'jpg',
                    'png',
                ]
            ),
            validate_foto_base
        ],
        null=True,
        blank=True,
        verbose_name="Фон",
        help_text="Загрузите фон для магазина (опционально)"
    )
    address = models.URLField(
        max_length=400,
        verbose_name="Адрес",
        help_text="Введите полный адрес магазина (ссылку)"
    )
    indicate_address = models.BooleanField(
        default=True,
        blank=True,
        verbose_name="Указать адрес",
        help_text="Укажите, нужно ли отображать адрес магазина"
    )
    ban = models.BooleanField(
        default=False,
        blank=True,
        verbose_name="Бан",
        help_text="Укажите, заблокировать ли магазин"
    )
    number_of_complaints = models.PositiveIntegerField(
        default=0,
        blank=True,
        verbose_name="Количество жалоб",
        help_text="Количество жалоб, поданных на магазин"
    )
    link = models.URLField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="Ссылка",
        help_text="Введите ссылку на магазин (опционально)"
    )
    date_of_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания магазина"
    )
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name="Пользователь",
        help_text="Пользователь, создавший магазин"
    )
    average_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=Decimal('0.00'),
        blank=True,
        validators=[
            MaxValueValidator(5.0),
            MinValueValidator(0.0)
        ],
        verbose_name="Рейтинг",
        help_text="Оценка от 0.00 до 5.00"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "магазин"
        verbose_name_plural = "магазины"


class Complaint(models.Model):
    text = models.TextField(
        max_length=1000,
        verbose_name="Текст жалобы",
        help_text="Введите текст жалобы (максимум 1000 символов)"
    )
    shop = models.ForeignKey(
        Shop,
        on_delete=models.PROTECT,
        verbose_name="Магазин",
        help_text="Выберите магазин, на который подана жалоба"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Пользователь",
        help_text="Пользователь, подавший жалобу"
    )
    screenshot = models.ImageField(
        upload_to=path_screenshot_complaint,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'jpg',
                    'png',
                ]
            ),
            validate_foto_base
        ],
        null=True,
        blank=True,
        verbose_name="Скриншот",
        help_text="Загрузите скриншот, подтверждающий жалобу (опционально)"
    )
    complaint_processed = models.BooleanField(
        blank=True,
        default=False,
        verbose_name="Жалоба обработана",
        help_text="Укажите, была ли жалоба обработана"
    )
    date_writing = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата написания",
        help_text="Дата и время написания жалобы"
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "жалобу"
        verbose_name_plural = "жалобы"
        unique_together = ('user', 'shop')


class Rating(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Пользователь, оставивший оценку"
    )
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        verbose_name="Магазин",
        help_text="Магазин, который был оценен"
    )
    number_rating = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ],
        verbose_name="Оценка",
        help_text="Оценка магазина от 1 до 5"
    )
    comment = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name="Комментарии для магазина"
    )
    date_writing = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата написания",
        help_text="Дата и время написания отзыва"
    )
    update_to = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
        help_text="Дата и время последнего обновления отзыва"
    )

    def __str__(self):
        return f"Пользователь: {self.user.username}\nМагазин: {self.shop.title}"

    class Meta:
        verbose_name = "рейтинг"
        verbose_name_plural = "рейтинги"
        unique_together = ('user', 'shop')
