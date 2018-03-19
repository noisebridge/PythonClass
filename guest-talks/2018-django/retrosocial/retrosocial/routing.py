from channels.routing import ProtocolTypeRouter, URLRouter

from users import routing


application = ProtocolTypeRouter({
    'websocket': URLRouter(
        routing.websocket_urlpatterns
    )
})
