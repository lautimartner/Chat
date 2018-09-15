class ChatRoom(self):
    def __init__(self, room_name, owner):
        self.room_name = room_name
        self.owner = owner
        self.wait_list = []
        self.confirmed_list= []

   
