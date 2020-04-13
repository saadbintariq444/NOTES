from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import notes.routing

# configuration of channels socket for our application
# connect consymer with main routing

application = ProtocolTypeRouter({
   'websocket' : AuthMiddlewareStack(
      URLRouter(
        notes.routing.websocket_urlpatterns
        )
    )
})

