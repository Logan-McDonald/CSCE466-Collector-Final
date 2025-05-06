import os
import django

from channels.routing      import ProtocolTypeRouter, URLRouter
from channels.auth         import AuthMiddlewareStack
from django.core.asgi      import get_asgi_application

from collector_backend import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collector_backend.settings')
django.setup()

application = ProtocolTypeRouter({
    # HTTP goes to Django’s normal ASGI app:
    "http": get_asgi_application(),

    # WebSocket goes through Channels, with auth:
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
