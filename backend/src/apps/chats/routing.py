from django.urls import path

from .consumer import MessageConsumer, NotificationConsumer

ws_urlpatterns = [
    path('ws/chat/<int:chat_id>', MessageConsumer.as_asgi()),
    path('ws/notification', NotificationConsumer.as_asgi())
]
