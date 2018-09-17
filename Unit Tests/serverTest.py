import unittest,sys
sys.path.append('home/lautimartner/Documents/Modelado/Chat/Model')
from Model.client import Client
from Model.User import User
from Model.ChatRoom import Chatroom
from Model.server import Server

serv = Server(("127.0.0.1",54004))
serv.enable(2)
user = User("Test","ACTIVE")
class serverTest(unittest.TestCase):
 
    def test_getAddress(self):
        self.assertEqual(serv.getAddress(),("127.0.0.1",54004))
    
    def test_getSocket(self):
        self.assertEqual(serv.getSocket(),serv.socket)
        serv.socket.close()
    
    def test_get_addConnUsers(self):
        serv.addConnectedUser(user)
        usr=serv.getConnUsers()
        self.assertEqual(usr[0],user)
    
    def test_setAddress(self):
        serv.setAddress(("127.0.0.1",53000))
        self.assertEqual(serv.getAddress(),("127.0.0.1",53000))
    
    def test_get_addChatRoom(self):
        chatroom = Chatroom("sala",user)
        serv.addChatroom(chatroom)
        ch = serv.getChatroom_list()
        self.assertEqual(ch[0],chatroom)
    
    def test_enable(self):
        self.assertEqual(None, "no se como probar esto")
        
    
    def broadcastTest(self):
        self.assertEqual(None, "")
        

if __name__ == '__main__':
    serv.disable()
    unittest.main()
