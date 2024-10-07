from decimal import Decimal
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.db import models

from ..base.services import path_photo_product
from ..base.validators import validate_foto_size_product, validate_file_size_avatar
from ..shops.models import Shop

User = get_user_model()


class Product(models.Model):
    CURRENCY = [
        ("KGS", "СОМ"),
        ("USD", "ДОЛЛАР")
    ]

    title = models.CharField(
        max_length=100,
        verbose_name="Название товара",
        help_text="Введите название продукта (макс. 100 символов)"
    )
    description = models.TextField(
        max_length=400,
        verbose_name="Описание",
        help_text="Введите описание продукта (макс. 400 символов)"
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена",
        help_text="Укажите цену продукта"
    )
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY,
        verbose_name="Валюта",
        help_text="Выберите валюту для цены продукта"
    )
    category = models.ForeignKey(
        "SubCategory",
        on_delete=models.PROTECT,
        verbose_name="Подкатегория",
        help_text="Выберите подкатегорию продукта"
    )
    shop = models.OneToOneField(
        Shop,
        on_delete=models.PROTECT,
        verbose_name="Магазин",
        help_text="Укажите магазин, в котором продается продукт"
    )
    product_rating = models.DecimalField(
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
        return f"{self.title} - {self.price} {self.get_currency_display()}"

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"


class ProductFoto(models.Model):
    photo = models.ImageField(
        upload_to=path_photo_product,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'jpg',
                    'png',
                ]
            ),
            validate_foto_size_product
        ],
        verbose_name="Фото продукта",
        help_text="Загрузите изображение продукта"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        help_text="Выберите продукт, к которому относится фото"
    )

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "фото продукта"
        verbose_name_plural = "фотографии продуктов"


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Введите название категории (макс. 100 символов)"
    )
    icon = models.ImageField(
        upload_to='icons/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'png',
                ],
                message="Разрешен только формат PNG"
            ),
            validate_file_size_avatar
        ],
        verbose_name = "Иконка",
        help_text = "Загрузите иконку в формате PNG. Размер файла не должен превышать установленный лимит 0.5MB."
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "категории"


class SubCategory(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название подкатегории",
        help_text="Введите название подкатегории (макс. 100 символов)"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Выберите категорию для подкатегории"
    )
    icon = models.ImageField(
        upload_to='icons/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'png',
                ],
                message="Разрешен только формат PNG"
            ),
            validate_file_size_avatar
        ],
        verbose_name = "Иконка",
        help_text = "Загрузите иконку в формате PNG. Размер файла не должен превышать установленный лимит 0.5MB."
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "подкатегорию"
        verbose_name_plural = "подкатегории"


class ProposalNewCategory(models.Model):
    text = models.TextField(
        max_length=700,
        verbose_name="Предложение",
        help_text="Введите ваше предложение для новой категории (макс. 700 символов)"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Пользователь",
        help_text="Выберите пользователя, сделавшего предложение"
    )

    def __str__(self):
        return f"Предложение от {self.user.username}: {self.text[:50]}..."  # Возвращает первые 50 символов текста

    class Meta:
        verbose_name = "предложение"
        verbose_name_plural = "предложении"


class ProductRating(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Пользователь, оставивший оценку"
    )
    product = models.ForeignKey(
        Product,
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
        unique_together = ('user', 'product')
