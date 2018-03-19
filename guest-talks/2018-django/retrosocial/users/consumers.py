from channels.generic.websocket import WebsocketConsumer


class FeedConsumer(WebsocketConsumer):
    def receive(self, text_data):
        print('receive', text_data)

