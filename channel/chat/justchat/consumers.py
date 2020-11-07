from channels.generic.websocket import WebsocketConsumer
import json

class chatconsumer(WebsocketConsumer):
    def connect(self):
        self.accept
    def disconnect(self, clsoe_code):
        pass
    def receive(self, text_data):
        text_data_jason=json.load(text_data)
        message=text_data_jason['message']

        self.send(text_data=json.dumps({'message':message}))