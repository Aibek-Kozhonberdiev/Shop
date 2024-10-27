from django.conf import settings
from django.core.mail import send_mail

from config.celery import app


@app.task
def send_key(user_email, key):
    send_mail(
        "test",
        f"test: {key}",
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False
    )
