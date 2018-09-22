import socket
import sys
from ChatRoom import Chatroom
from User import User
from _thread import *

class Server:
    """
    Clase para implementar el servidor, para correr hay que ejecutar esta clase con
    python3 server.py y cambiar los parametros a desear desde el main

    Atrributes
    ----------
    ip : str
        direccion ip
    port : int
        puerto
    socket : socket
        socket del servidor
    conn_users : list
        lista de usuarios conectados
    chatroom_list : list
        lista de salas en el servidor
    """
    def __init__(self, address):
            self.ip_address, self.port = address
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.conn_users = []
            self.chatroom_list= []
    

    def getAddress(self):
        """
        getter para address
        :return: tuple
            ip address y puerto

        """
        return self.address
    
    def getSocket(self):
        """
        getter para el socket
        :return: socket
        """
        return self.socket
    
    def getConnUsers(self):
        """
        regresa connected users
        :return: list
            lista de usuarios conectados
        """
        return self.conn_users
    
    def setAddress(self, new_address):
        """
        setter para address
        :param new_address: tuple
            address
        :return:  void
        """
        self.address=new_address
    
    def addConnectedUser(self, user):
        """
        agrega usuario conectado
        :param user: user
            nuevo ussario conectado
        :return: void
        """
        self.conn_users.append(user)
    
    def addChatroom(self, chatroom):
        """
        agrega sala de chat
        :param chatroom:
            nueva sala de chat

        :return:
        """
        self.chatroom_list.append(chatroom)
        
    def getChatroom_list(self):
        """
        getter para  la lista de salas
        :return: list
            sala de chat
        """
        return self.chatroom_list
    
    def enable(self, list_number):
        """
        prende el servidor y conecta la direccion ip a
        :param list_number:
        :return:
        """
        self.socket.bind((self.ip_address, self.port))
        self.socket.listen(list_number)
        print("Listening up to %d clients" %(list_number))
    
    def disable(self):
        with self.socket as s:
            s.close()
            print("Server has been closed")

    """Manages active clients using the agreed protocol messages"""
    def client_thread(self, curr_client_socket, add):
        i=0
        idd = False
        curr_status = None
        curr_username = None
        try:
            while True:
                message = curr_client_socket.recv(4096)
                message = message.decode()
                message_words = message.split()
                print(message_words[0])
                curr_user = User(curr_username, curr_status, curr_client_socket)

                if(message_words[0] == "IDENTIFY"):
                    identificarlo = True
                    if idd:
                        self.broadcast([curr_user], "Ya te identificaste")
                    if not idd:
                        for user in self.conn_users:
                            if user.getName() == message_words[1]:
                                self.broadcast([curr_user], "Ese nombre ya ha sido usado, usa otro")
                                identificarlo = False
                        if identificarlo:
                            curr_username = message_words[1]
                            curr_user.setName(curr_username)
                            self.broadcast([curr_user], "Te has idenfiticado")
                            self.addConnectedUser(curr_user)
                            idd = True
                elif(i==0 and not idd):
                    curr_client_socket.send(b"Identificate")

                elif(message_words[0] == "STATUS" and idd):
                    if message_words[1].decode() not in ["ACTIVE", "AWAY", "BUSY"]:
                        curr_client_socket.send(b"Opcion Invalida. Opciones validas: ACTIVE, AWAY, BUSY")
                    else:
                        curr_user.setStatus(curr_status)
                        self.broadcast(curr_client_socket, "Tu status ha cambiado")

                elif(message_words[0] == "USERS" and idd):
                    print("USERS")
                    msg = ''
                    for user in self.conn_users:
                        msg = msg + ' ' + user.getName()
                    self.broadcast([curr_user], msg)

                elif(message_words[0] == "CREATEROOM" and idd):
                    room = Chatroom(message_words[1], curr_user)
                    self.chatroom_list.append(room)
                    room.addToConfirmedList(curr_user)

                elif(message_words[0] == "INVITE" and idd ):
                    curr_chatroom = ''
                    encontrado = False
                    for chatroom in self.chatroom_list:
                        if (chatroom.getRoomName() == message_words[1]):
                            encontrado = True
                            curr_chatroom = chatroom
                    if encontrado and curr_chatroom.getOwner().getName() != curr_username:
                        mess = "Solo el propietario de la sala puede invitar a otros usuarios"
                        curr_client_socket.send(mess.encode())
                        continue
                    if (encontrado == False):
                        msg = "La sala %s no existe" % message_words[1]
                        curr_client_socket.send(msg.encode())
                        continue
                    for invi_username in message_words[2:]:
                        for users in self.conn_users:
                            if (users.getName() == invi_username):
                                curr_chatroom.addToWaitlist(users)
                                msg = "Has sido invitado a %s" % curr_chatroom.getRoomName()
                                self.broadcast([users], msg)

                elif (message_words[0] == "PUBLICMESSAGE" and idd):
                    print("public message")
                    self.broadcast(self.conn_users, self.concat_list_into_str(message_words[1:]))

                elif idd and (message_words[0] == "ROOMESSAGE" or message_words[0] == "MESSAGE"):
                    receiver_list = self.receiver_det(message_words[0], message_words[1])
                    self.broadcast(receiver_list, curr_username + ': ' + self.concat_list_into_str(message_words[2:]))

                elif (message_words[0] == "DISCONNECT"):
                    self.disconnect(curr_client_socket, curr_username)
                    break
                    return

                elif (message_words[0] == "JOINROOM" and idd):
                    addable_to_confirmlist = False
                    for chatrooms in self.chatroom_list:
                        print(chatrooms.getRoomName() + message_words[1])
                        if (chatrooms.getRoomName() == message_words[1]):
                            print("Sala encontrada")
                            for users in chatrooms.getWaitList():
                                if (users.getName() == curr_username):
                                    chatrooms.moveUserfromWaitlistToConfirmedlist(users)
                                    print(str(chatrooms.confirmed_list))
                                    addable_to_confirmlist = True
                                    self.broadcast(self.receiver_det("ROOMESSAGE",chatrooms),"%s se ha unido a esta sala" %curr_username)
                    if not addable_to_confirmlist:
                        self.broadcast([curr_user], "No te puedes unir a esta sala")
                else:
                    val_msg = b"PUBLICMESSAGE, MESSAGE, ROOMESSAGE, JOINROOM, CREATEROOM, DISCONNECT, IDENTIFY, INVITE, STATUS, USERS"
                    self.broadcast([curr_user], b"No te has identificado o eso no es parte del protocolo. Mensajes validos: %b " %val_msg)
                i+=1
        except Exception as e:
            print(e.__doc__)
            print(e)
        except KeyboardInterrupt:
            self.disconnect(curr_client_socket, curr_username)
        except BrokenPipeError:
            self.disconnect(curr_client_socket, curr_username)

    '''Determines who a message gonna be sent to based on protocol messages'''
    def receiver_det(self, protocol_message, receivers):
        end_receivers =[]
        if (protocol_message == "MESSAGE"):
            for user in self.conn_users:
                if (user.getName()==receivers):
                    end_receivers.append(user)
                    break

        elif (protocol_message=="ROOMESSAGE"):
            for chatrooms in self.chatroom_list:
                if(chatrooms.getRoomName()==receivers):
                    for user in chatrooms.getConfirmedList():
                        print(user.getName())
                        end_receivers.append(user)
        return end_receivers

    """Concatenates lists into strings"""
    def concat_list_into_str(self, list):
        msg = ''
        for string in list:
            msg+= ' ' +  str(string)
        return msg

    def disconnect(self, curr_client_socket, username):
        for user in self.conn_users:
            if user.getName() == username:
                print(username + " se ha desconectado")
                self.conn_users.remove(user)
                curr_client_socket.close()

    '''Sends message to receivers'''
    def broadcast(self, receivers, message):
        for user in receivers:
            try:
                if type(message) != bytes:
                    message = message.encode()
                user.getClientSocket().send(message)
            except:
                user.getClientSocket().send(b"No se pudo enviar el mensaje")
        
    '''Manages threads'''
    def client_thread_admin(self,n):
        self.enable(n)
        try:
            while True: #cambiar despues
                curr_client_socket, curr_client_address=self.socket.accept()
                print("Se ha conectado %s" %str(curr_client_address))
                start_new_thread(self.client_thread, (curr_client_socket, curr_client_address))

        except:
            print("Servidor cerrado")
        
if __name__ == '__main__':
    server = Server(("0.0.0.0",int(input("Pon el puerto: "))))
    server.client_thread_admin(1) #Poner numero de clientes esperados a ser conectados por el servidor, cambiar a gusto

