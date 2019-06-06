import json

class Message:
    def __init__(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        self.message = body['message']
        self.workspace = body['workspace']
        self.channel = body['channel']
        self.username = body['sender']
        self.action = self.message.split(" ")[0]

    def client(self):
        client = self.workspace + "+" + self.channel
        return client

    def argument(self):
        try:
            argument = self.message.split(" ")[1]
        except IndexError as e:
            argument = "0"
        return argument




