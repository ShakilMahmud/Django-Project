from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
import chat.justchat.routing

application= ProtocolTypeRouter{
    'websocket':AuthMiddlewareStack( URLRouter(chat.justchat.routing.Websocket_urlpatterns)),

}

