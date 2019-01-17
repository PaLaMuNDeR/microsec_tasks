from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from .consumers import TemperatureConsumer

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        # Matches the 'settings.ALLOWED_HOSTS' verification for websockets
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r"^temperature/", TemperatureConsumer),

                ]
            )

        )

    )
})
