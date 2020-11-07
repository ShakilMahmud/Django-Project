from channels.generic.websocket import WebsocketConsumer
from . import consumers

Websocket_urlpatterns=[
    re_path(r'ws/chat/(?P<room_name>\w+)/$',consumers.chatconsumer)
]