
class Controller:

    def __init__(self, client):
        self.client = client

    def updateClient(self, command):

        self.client.messageManager(command)