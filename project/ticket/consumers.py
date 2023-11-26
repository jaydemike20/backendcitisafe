from channels.generic.websocket import WebsocketConsumer


from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('broadcast', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('broadcast', self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send the message to the group
        await self.send(text_data=json.dumps({'message': message}))

    async def send_notification(self, event):
        # Send the notification to the WebSocket
        await self.send(text_data=event['message'])

class MyConsumer(WebsocketConsumer):
    groups = ["broadcast"]

    def connect(self):
        pass

    def receive(self):
        pass

    def disconnect(self):
        pass


class TestConsumer(WebsocketConsumer):
    def connect(self):
        # Called on connection.
        # To accept the connection call:
        self.accept()
        # Or accept the connection and specify a chosen subprotocol.
        # A list of subprotocols specified by the connecting client
        # will be available in self.scope['subprotocols']
        # To reject the connection, call:
        self.close()

    def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        # Want to force-close the connection? Call:
        self.close()
        # Or add a custom WebSocket error code!

    def disconnect(self, close_code):
        # Called when the socket closes
        pass