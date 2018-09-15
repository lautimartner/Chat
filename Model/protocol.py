from enum import Enum
class Protocol(Enum)
    IDENTIFY = "IDENTIFY" #[username] | Este comando identifica al usuario, username será el nombre del usuario, ejemplo: IDENTIFY Kimberly
    STATUS = "STATUS" #userstatus | Este comando asignará el estado al usuario, userstatus es uno de los tres posibles estados, ejemplo: STATUS AWAY
    USERS = "USERS" # Mostrará los usuarios identificados, ejemplo: USERS
    MESSAGE = "MESSAGE"#[username] [messageContent] | Enviará un mensaje privado a username, y el mensaje será messageContent, ejemplo: MESSAGE Luis Hola Luis
    PUBLICMESSAGE = "PUBLICMESSAGE" #[messageContent] | Enviará el mensaje a todos los usuarios identificados, ejemplo: PUBLICMESSAGE Hola a todos!
    CREATEROOM = "CREATEROOM" # [roomname] | Se creará una sala en el servidor con nombre roomname y el dueño de la sala será el que la creó, ejemplo: CREATEROOM SALA1
    INVITE = "INVITE" # [roomname] [username1 username2,...] | Enviará una invitación a la lista de usuarios para unirse a la sala roomname, ejemplo: INVITE SALA1 LUIS KIM FER
    JOINROOM = "JOINROOM" # [roomname] | Aceptará la invitación a la sala roomname que fue invitado, JOINROOM SALA1
    ROOMESSAGE = "ROOMESSAGE" # [roomname] [messageContent] | Enviará el mensaje a todos los usuarios dentro de esa sala, ejemplo: ROOMESSAGE sala1 Hola sala1!
    DISCONNECT = "DISCONNECT" #El usuario se desconecta del servidor, ejemplo: DISCONNECT
