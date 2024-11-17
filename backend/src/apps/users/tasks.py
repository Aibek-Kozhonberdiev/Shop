import http.client
import json
from django.conf import settings
from django.core.mail import send_mail

from config.celery import app


@app.task
def send_key_email(user_email, key):
    send_mail(
        "test",
        f"test: {key}",
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False
    )

@app.task
def send_phone(number, text, term):
    conn = http.client.HTTPSConnection("web.it-decision.com")
    headers = {
        'Authorization': settings.PHONE_KEY,
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
    "phone": number,
    "sender": settings.NAME_SHOP,
    "text": text,
    "validity_period": term
    })
    conn.request("POST", "/v1/api/send-sms", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("uft-8")
