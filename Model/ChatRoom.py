class Chatroom:
    """
    Clase usada para representar una sala de chat

    Attributes
    ---------
    room_name : str
        nombre de la sala
    owner : user
        usuario propietario de la sala
    wait_list : lista de usuarios
        lista de usuarios invitados que aun no se han unido a la sala
    confirmed_list : lista de usuarios
        lista de usuario unidos a la sala, si les llegan mensajes



    """
    def __init__(self, room_name, owner):
        self.room_name = room_name
        self.owner = owner
        self.wait_list = []
        self.confirmed_list= []


    def addToWaitlist(self,user):
        """
        Agrega usuario a la lista de espera
        :param user: user
            usuario invitado
        :return: void
        """
        self.wait_list.append(user)

    def addToConfirmedList(self, user):
        """
        Agrega usuario a la lista de confirmados en la sala
        :param user: user
            usuario agregado a la lista de verdad
        return: void
        """
        self.confirmed_list.append(user)

    def moveUserfromWaitlistToConfirmedlist(self, change_user):
        """
        Mueve a algun usuario de la lista de espera a la lista de confirmados

        :param change_user:  user
            usuario movido
        :return: void
        """
        for user in self.wait_list:
            if (user.getName() == change_user.getName()):
                self.confirmed_list.append(change_user)
                self.wait_list.remove(user)

