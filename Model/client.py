import socket
import sys
import a
class Client:
    def __init__(self, socket, address, user, chatrooms, ):
        self.address =address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.user = user
        self.chatrooms = []
    
