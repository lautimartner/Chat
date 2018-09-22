from PyQt5 import QtCore, QtGui, QtWidgets
from View.guidef import GUI
import sys

class View(QtWidgets.QMainWindow):

    def __init__(self, controller, client):
        super(View,self).__init__()
        self.controller = controller
        self.client = client
        self.ui = GUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.send)
        self.client.listeners.append(self.received)

    def received(self, msg):
        self.ui.textEdit.append(msg)

    def send(self):
        string = self.ui.lineEdit.text()
        self.ui.textEdit.append(string)
        self.ui.lineEdit.clear()
        self.controller.updateClient(string)

