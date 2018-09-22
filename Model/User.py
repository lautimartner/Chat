import random
class User:
    """
    Clase usuario, usada para representar a un usuario

    Attributes
    ----------
    name : str
        nombre de usuario
    status : str
        status del usuario
    client_socket : socket
        socket del cliente asociado al usuario

    Methods
    -------
    getName()
        regresa el nombre
    getStatus()
        regresa el status
    setName(str)
        cambia el nombre
    setStatus(status)
        cambiar el status
    getClientSocket()
        regresa el socket



    """
    def __init__(self, name, status, client_socket):
        self.name = name
        self.status = status
        self.client_socket = client_socket

    def getName(self):
        """

        :return: el nombre del usuario
        """
        return self.name
    
    def getStatus(self):
        """

        :return: status del usuario
        """
        return self.status

    def setName(self,nname):
        """

        :param nname: str
            nuevo nombre
        :return: void
        """
        self.name=nname
    
    def setStatus(self,sstatus):
        """

        :param sstatus: str
            nuevo status
        :return:  void
        """
        self.status=sstatus

    def getClientSocket(self):
        """

        :return: socket
            nuevo socket del cliente
        """
        return self.client_socket
