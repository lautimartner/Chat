import socket, sys
class Client:
    def __init__(self, serv_address, user, socket):
        self.address = serv_address
        if (socket==None):
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.socket = socket
        self.user = user
        self.chatrooms = []

        
    def getAddress(self):
        return self.address
        
    def getSocket(self):
        return self.socket
    
    def getUser(self):
        return self.user
    
    def setUser(self, user):
        self.user=user
    
    def setAddress(self, new_serv_address):
        self.address = new_serv_address
    
    def addChatroom(self, new_chatroom):
        self.chatrooms.append(new_chatroom)
        
    def getChatroom(self):
        return self.chatrooms
    
    def connToServer(self):
        with self.socket as s:
            s.connect(self.address)
            print("Connected to server with IP: %s and port: %d" % (self.address[0],self.address[1]))
            
    def sendPriMessage(self, ):
        return 0
    
    def sendPubMessage(self):
        return 0
    
if __name__ == '__main__':
    print("Todo bien")
