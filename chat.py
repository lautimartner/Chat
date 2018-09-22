from Model.client import Client
from Model.User import User
from Controller.controller import Controller
import sys
import threading
from PyQt5 import QtWidgets
from View.view import View
class StartChat(QtWidgets.QApplication):
    def __init__(self, system_argv):
        super(StartChat, self).__init__(system_argv)
        self.client = Client(None,None,None)
        self.controller = Controller(self.client)
        self.gui = View(self.controller, self.client)
        self.client.connToServer(None)
        main_thread = threading.Thread(target=self.client.input_manager)
        main_thread.setDaemon(True)
        main_thread.start()
        self.gui.show()

if __name__ == '__main__':
    newChat = StartChat(sys.argv)
    sys.exit(newChat.exec_())