import unittest
import socket
import sys
sys.path.append('home/lautimartner/Documents/Modelado/Chat/Model')
from Model.User import User
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user = User("pedro", "ACTIVE", socket)
class UserTest(unittest.TestCase):
    def test_getName(self):
        self.assertEqual("pedro", user.getName())

    def test_getStatus(self):
        self.assertEqual("ACTIVE", user.getStatus())

    def test_setName(self):
        user.setName("caca")
        self.assertEqual("caca", user.getName())

    def test_setStatus(self):
        user.setStatus("AWAY")
        self.assertEqual("AWAY", user.getStatus())

    def test_getClientSocket(self):
        self.assertEqual(socket, user.getClientSocket())


socket.close()
if __name__ == '__main__':
    unittest.main()