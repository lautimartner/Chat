import socket
import sys
import select
class Client:
    def __init__(self, serv_address, user, sockets):
        if (sockets is None):
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.socket = sockets
        self.user = user
        self.address = serv_address
        self.listeners = []

        

    
    def connToServer(self, ip):
        if ip is None:
            ip = str(input("Pon la direccion ip del servidor: "))
        port = int(input("Pon el puerto: "))
        self.setAddress((ip, port))
        self.socket.connect(self.address)
        print("Connected to server with IP: %s and port: %d" % (self.address[0],self.address[1]))

    """Concatenates lists into strings"""
    def concat_list_into_str(self, list):
        msg = ''
        for string in list:
            msg += ' ' + str(string)
        return msg

    def sendPriMessage(self, message):
        message = message.split()
        fin_mess = "MESSAGE " + self.concat_list_into_str(message)
        return fin_mess

    def sendPubMessage(self, message):
        split_mess = message.split()
        fin_mess = "PUBLICMESSAGE " + self.concat_list_into_str(split_mess)
        return fin_mess

    def sendRoomMess(self, message):
        message = message.split()
        fin_mess =  "ROOMESSAGE " + self.concat_list_into_str(message)
        return fin_mess

    def input_manager(self):
        conn = True
        try:
            while True and conn:
                input_socklist = [sys.stdin, self.socket]
                read_sockets, write_socket, error_socket = select.select(input_socklist, [], [])
                for csocket in read_sockets:
                    if csocket == self.socket:
                        message = self.socket.recv(2048)
                        msg = message.decode()
                        if not message:
                            conn = False
                        else:

                            self.update(msg)
                            if msg== "d":
                                conn = False
                                self.socket.send("DISCONNECT")


        except:
            print ("Te has desconectado")
            self.socket.close()

    """Translates short strings into protocol messages and sends it to the server"""
    def messageManager(self, prot_message):
        trans = prot_message.split()
        if trans[0] == "id":
            fin_mess = "IDENTIFY " + trans[1]
        elif trans[0] == "s":
            fin_mess = "STATUS " + trans[1]
        elif trans[0] == "u":
            fin_mess = "USERS"
        elif trans[0] == "pm":
            fin_mess = self.sendPriMessage(self.concat_list_into_str(trans[1:]))
        elif trans[0] == "rm":
            fin_mess = self.sendRoomMess(self.concat_list_into_str(trans[1:]))
        elif trans[0] == "m":
            fin_mess = self.sendPubMessage(self.concat_list_into_str(trans[1:]))
        elif trans[0] == "cm":
            fin_mess = "CREATEROOM "+ trans[1]
        elif trans[0] == "i":
            fin_mess = "INVITE " + self.concat_list_into_str(trans[1:])
        elif trans[0] == "j":
            fin_mess = "JOINROOM " + trans[1]
        elif trans[0] == "d":
            fin_mess = "DISCONNECT"

        else:
            fin_mess = "Mensaje invalido"
        self.socket.send(fin_mess.encode())

    def update(self, event):
        for listener in self.listeners:
            listener(event)


if __name__ == '__main__':
    client = Client(None,None,None)
    client.connToServer('192.168.1.241')
    client.input_manager()
    client.getSocket().close()
    print("Todo bien")

