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




    """
    def __init__(self, name, status, client_socket):
        self.name = name
        self.status = status
        self.client_socket = client_socket


