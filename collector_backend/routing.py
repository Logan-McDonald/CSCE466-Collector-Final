from django.urls import re_path
from messaging.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_key>[\w_]+)/$', ChatConsumer.as_asgi()),
]
