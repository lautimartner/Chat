import random
class User:
    def __init__(self, name, status, client_socket):
        self.name = name
        self.status = status
        self.client_socket = client_socket

    def getName(self):
        return self.name
    
    def getStatus(self):
        return self.status
    
    def getUniqueNumber(self):
        return self.unique_number
    
    def setName(self,nname):
        self.name=nname
    
    def setStatus(self,sstatus):
        self.status=sstatus

    def getClientSocket(self):
        return self.client_socket
