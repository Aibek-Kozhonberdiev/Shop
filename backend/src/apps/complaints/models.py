from django.contrib.auth import get_user_model
from django.db import models

from ..shops.models import Shop


User = get_user_model()

class Complain(models.Model):
    description = models.CharField()
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)


class Support(models.Model):
    title = models.CharField()
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
