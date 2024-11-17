from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models

from ..base.services import path_image_message, FileSizeValidator

User = get_user_model()


class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name='chats')


class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(
        null=True, blank=True, upload_to=path_image_message,
        validators=[FileSizeValidator(max_size_mb=1.5), FileExtensionValidator(allowed_extensions=['png', 'jpg', 'pdf', 'docs', 'xls', 'xlsx', 'pptx'])]
    )
    is_read = models.BooleanField(default=False, blank=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
