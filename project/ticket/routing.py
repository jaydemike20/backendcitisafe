# routing.py

from django.urls import re_path

from .consumers import MyConsumer, TestConsumer, NotificationConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

websocket_urlpatterns = [
    re_path(r'ws/notification/$', MyConsumer.as_asgi()),
    re_path(r'ws/test/', TestConsumer.as_asgi()),
    re_path(r'ws/ticketnotification/', NotificationConsumer.as_asgi()),

]


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
