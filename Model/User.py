class User:
    def __init__(self, conn_socket, name, status, unique_number):
        self.conn_socket = conn_socket
        self.name = name
        self.status = status
        self.unique_number = unique_number

    
