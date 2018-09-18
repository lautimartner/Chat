import socket
import sys
from ChatRoom import Chatroom
from User import User
from _thread import *

class Server:
    def __init__(self, address):
            self.ip_address, self.port = address
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.conn_users = []
            self.chatroom_list= []
    
    '''Getters, setters and functionality functions'''
    def getAddress(self):
        return self.address
    
    def getSocket(self):
        return self.socket
    
    def getConnUsers(self):
        return self.conn_users
    
    def setAddress(self, new_address):
        self.address=new_address
    
    def addConnectedUser(self, user):
        self.conn_users.append(user)
    
    def addChatroom(self, chatroom):
        self.chatroom_list.append(chatroom)
        
    def getChatroom_list(self):
        return self.chatroom_list
    
    def enable(self, list_number):
        self.socket.bind((self.ip_address, self.port))
        self.socket.listen(list_number)
        print("Listening up to %d clients" %(list_number))
    
    def disable(self):
        with self.socket as s:
            s.close()
            print("Server has been closed")
        
    def client_thread(self, curr_client_socket, add):
        i=0

        curr_status = None
        curr_username = None
        while True:
            message = curr_client_socket.recv(4096)
            message = message.decode()
            message_words = message.split()
            curr_user = User(curr_username, curr_status, curr_client_socket)
            self.addConnectedUser(curr_user)

            if (i==0 and curr_username == None):
                curr_client_socket.send(b"Identificate")
            elif(message_words[0] == "IDENTIFY"):
                curr_username = message_words[1]
                curr_user.setName(curr_username)
                self.broadcast([curr_user], "Te has idenfiticado")

            elif(message_words[0] == "STATUS"):
                curr_status = message_words[1]
                curr_user.setStatus(curr_status)
                self.broadcast(curr_client_socket, "Tu status ha cambiado")

            elif(message_words[0] == "USERS"):
                print("USERS")
                msg = ''
                for user in self.conn_users:
                    msg = msg + ' ' + user.getName()
                self.broadcast([curr_user], msg)

            elif(message_words[0] == "CREATEROOM"):
                room = Chatroom(message_words[1], curr_user)
                self.chatroom_list.append(room)
                room.addToConfirmedList(curr_user)

            elif(message_words[0] == "INVITE"):
                curr_chatroom = None
                for chatroom in self.chatroom_list:
                    encontrado = False
                    if (chatroom.getRoomName() == message_words[1]):
                        encontrado = True
                        curr_chatroom = chatroom
                if (encontrado == False):
                    msg = "La sala %s no existe" % message_words[1]
                    curr_client_socket.send(msg.encode())
                for invi_username in message_words[2:]:
                    for users in self.conn_users:
                        if (users.getName() == invi_username):
                            curr_chatroom.addToWaitlist(users)
                            msg = "Has sido invitado a %s" % curr_chatroom.getRoomName()
                            self.broadcast([users], msg)

            elif (message_words[0] == "PUBLICMESSAGE"):
                print("public message")
                self.broadcast(self.conn_users, self.concat_list_into_str(message_words[1:]))

            elif(message_words[0] == "ROOMESSAGE" or message_words[0] == "MESSAGE"):
                receiver_list = self.receiver_det(message_words[0], message_words[1])
                if message_words[0] != "MESSAGE" and curr_user in receiver_list:
                    receiver_list.remove(curr_user)
                self.broadcast(receiver_list,   self.concat_list_into_str(message_words[2:]))

            elif (message_words[0] == "DISCONNECT"):
                curr_client_socket.close()
                self.conn_users.remove(curr_user)
                break

            elif (message_words[0] == "JOINROOM"):
                for chatrooms in self.chatroom_list:
                    if (chatrooms.getRoomName() == message_words[1]):
                        addable_to_confirmlist = False
                        for users in chatrooms.getWaitList():
                            if (users.getName() == curr_username):
                                chatrooms.moveUserfromWaitlistToConfirmedlist(users)
                        self.broadcast(self.receiver_det("ROOMESSAGE",chatrooms),"%s se ha unido a esta sala" %curr_username)
            else:
                self.broadcast([curr_user], b"Eso no es parte del protocolo")
            i+=1

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
                        end_receivers.append(user)
        return end_receivers

    def concat_list_into_str(self,list):
        msg = ''
        for string in list:
            msg+= ' ' +  str(string)
        return msg



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
        while True: #cambiar despues
            curr_client_socket, curr_client_address=self.socket.accept()
            print("Se ha conectado %s" %str(curr_client_address))
            start_new_thread(self.client_thread, (curr_client_socket, curr_client_address))

        
if __name__ == '__main__':
    server = Server(('192.168.25.87',1235))
    server.client_thread_admin(100)

    print("Todo bien")

