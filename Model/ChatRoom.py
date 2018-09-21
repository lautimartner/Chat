class Chatroom:
    def __init__(self, room_name, owner):
        self.room_name = room_name
        self.owner = owner
        self.wait_list = []
        self.confirmed_list= []


    def getRoomName(self):
        return self.room_name

    def getOwner(self):
        return self.owner

    def getWaitList(self):
        return self.wait_list

    def getConfirmedList(self):
        return self.confirmed_list

    def setRoomName(self, name):
        self.room_name=name

    def addToWaitlist(self,user):
        self.wait_list.append(user)

    def addToConfirmedList(self, user):
        self.confirmed_list.append(user)

    def moveUserfromWaitlistToConfirmedlist(self, change_user):
        for user in self.wait_list:
            if (user.getName() == change_user.getName()):
                self.confirmed_list.append(change_user)
                self.wait_list.remove(user)

