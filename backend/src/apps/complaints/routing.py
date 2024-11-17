from django.urls import path

from .consumer import ComplaintConsumer

ws_urlpatterns = [
    path('ws/complaint/', ComplaintConsumer.as_asgi())
]
