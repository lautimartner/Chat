import socket, sys, unittest
sys.path.append('home/lautimartner/Documents/Modelado/Chat/Model')
from Model.client import Client
from Model.User import User
from Model.ChatRoom import Chatroom

class clientTest(unittest.TestCase):

    def test_getAddress(self):
        user = User("Test", "ACTIVE")
        cliente = Client(('127.0.0.1', 54000), user)
        self.assertEqual(cliente.getAddress(), ('127.0.0.1',54000))
        
    def test_getSocket(self):
        user = User("Test", "ACTIVE")
        cliente = Client(('127.0.0.1', 54000), user)
        self.assertEqual(cliente.getSocket(),cliente.socket)
        cliente.socket.close()
   
    def test_getUser(self):
        user = User("Test", "ACTIVE")
        cliente = Client(('127.0.0.1', 54000), user)
        self.assertEqual(cliente.getUser(),user)
   
    def test_setUser(self):
        user = User("Test", "ACTIVE")
        cliente = Client(('127.0.0.1', 54000), user)
        new_user = User("test","AWAY")
        cliente.setUser(new_user)
        self.assertEqual(cliente.getUser(), new_user)
   
    def test_setAddress(self):
        user = User("Test", "ACTIVE")
        cliente = Client(('127.0.0.1', 54000), user)
        cliente.setAddress(('127.0.0.1',58012))
        self.assertEqual(cliente.getAddress(),('127.0.0.1',58012))
        
    def test_get_addChatroom(self):
        user = User("Test", "ACTIVE")
        cliente = Client(('127.0.0.1', 54000), user)
        chatroom = Chatroom("sala",user)
        cliente.addChatroom(chatroom)
        ch = cliente.getChatroom()
        self.assertEqual(ch[0],chatroom)
        
    def test_connToServer(self):
        #no implementado aun
        self.assertEqual(None,None)
        
    #def sendPriMessageTest(self);
        
        
    #def sendPubMessage(self):


if __name__ == '__main__':
    cliente.g
    unittest.main()



    
