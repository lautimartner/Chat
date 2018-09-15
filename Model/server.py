import socket
import sys

class Servidor:
    def __init__(self, address, socket):
            self.address = address
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.conn_users = []
            self.chatroom_list= []
    






if __name__ == '__main__':



















	'''Enciende servidor'''
	def enable_server(self, num_clients):
		self.socket.bind(self.address)
		self.socket.listen(num_clients)
		print ("Server enabled and waiting for " + str(num_clients) + " clients")

	'''Acepta peticiones de conexion y aministra el hilo de cada cliente conectado al servidor'''
	def client_manager(self):
		while True:
			clientsock, claddress = self.socket.accept()
			conn_clients.append(clientsock)
			print(claddress, " has been added to the chatroom")


	def broadcast(self, receivers, message):
		while True:
			mensaje = clientsock.recv(10000)
			print(repr(recibido))


    def close_server(self):
	    self.socket.close()
		print("Closing server")



