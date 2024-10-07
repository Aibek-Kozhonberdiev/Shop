from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models

from ..base.services import path_image_message, path_file_message
from ..goods.models import Product, ProductRating

User = get_user_model()


class Chat(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name="Продукт",
        help_text="Продукт, связанный с чатом"
    )
    product_rating = models.ForeignKey(
        ProductRating,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Оценка продукта",
        help_text="Оценка продукта, если применимо"
    )
    create_to = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания чата"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="chats_sent",
        verbose_name="Покупатель",
        help_text="Обычный пользователь"
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="chats_received",
        verbose_name="Продавец",
        help_text="Пользователь, который продает товар"
    )

    def __str__(self):
        return f"Чат между {self.user.username} и {self.seller.username} о продукте {self.product.title}"

    class Meta:
        verbose_name = "чат"
        verbose_name_plural = "чаты"
        unique_together = ("user", "seller")
        ordering = ['-create_to']

    def clean(self):
        if self.product_rating:
            if self.product_rating.shop.user != self.seller:
                ValidationError("Только продавец может оставить сообщение об отзыве")
        super().clean()


class Message(models.Model):
    text = models.TextField(
        null=True,
        blank=True,
        max_length=300,
        verbose_name="Сообщение",
        help_text="Текст сообщения (макс. 300 символов)"
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=path_image_message,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'jpg',
                    'png'
                ]
            ),
        ],
        verbose_name="Изображение",
        help_text="Изображение в формате JPG или PNG"
    )
    file = models.FileField(
        null=True,
        blank=True,
        upload_to=path_file_message,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    'docx',
                    'pdf',
                    'txt'
                ]
            ),
        ],
        verbose_name="Файл",
        help_text="Файл документа (DOCX, PDF, TXT)"
    )
    create_to = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата отправки",
        help_text="Дата и время отправки сообщения"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="messages_sent",
        verbose_name="Отправитель",
        help_text="Пользователь, отправивший сообщение"
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="messages_received",
        verbose_name="Получатель",
        help_text="Пользователь, получивший сообщение"
    )
    is_read = models.BooleanField(
        default=False,
        blank=True,
        verbose_name="Прочитано",
        help_text="Отметьте, если сообщение было прочитано"
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.PROTECT,
        verbose_name="Чат",
        help_text="Чат, к которому относится сообщение"
    )

    def __str__(self):
        return f"Отправитель: {self.user.username}, Получатель: {self.user_recipient.username}, Текст: {self.text[:50]}..."

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"
        ordering = ['-create_to']

    def clean(self):
        if not self.text and not self.image and not self.file:
            raise ValidationError('Необходимо отправить либо текст, либо изображение, либо файл.')
        super().clean()
