from django.urls import path

from .consumer import SupportConsumer

ws_urlpatterns = [
    path('ws/consumer/', SupportConsumer.as_asgi())
]
