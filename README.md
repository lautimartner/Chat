# Chat

Proyecto para clase de Modelado y Programacion de Ciencias de la Computacion, Facultad de Ciencias, UNAM. 
Mi nombre es Ismael Lautaro Martner Varela
## Como clonarlo
git clone https://github.com/lautimartner/Chat.git
## Como ejecutarlo y usarlo
### Servidor
Dentro del directorio Chat/Model poner en la terminal python3 server.py. Despues va a pedirte por el puerto. La direccion 
ip esta puesta a 0.0.0.0 pero se puede cambiar en el main. Tambien si quieres cambiar el numero de conexiones posibles que 
acepta el servidor ponlo como parametro del metodo client_thread_admin.

### Pruebas unitarias
Dentro del directorio Chat/ ejecutar: python3 -m unittest Unit\ Tests.[module_name] donde module name es nombre del modulo sin el .py,
ejempli clientTest.py entonces el comando seria: python3 -m unittest Unit\ Tests.clientTest

### Cliente
Dentro del directorio Chat/ ejecutar python3 chat.py y despues poner la direccion ip y el puerto en la terminal. Si quieres omitir el poner la direccion ip cada vez
en la linea 14 de chat,py pon como argumento en una string la direccion ip en el metodo connToServer.

Perdon por poner lo siguiente aqui pero no me dio tiempo de ponerlo en la interfaz:
id [username]: identificarte con nombre username

u: imprime la lista de usuarios

s [estado]: cambiar tu estado a alguno de los 3 posibles

cm [chatroom_name]: crear sala con nombre chatroom_name

i [chatroom_name] [usernames]: invitar a usernames a chatroom_name


j [chatroom_name]: unirse a chatroom_name

m [message]: enviar message a todos los usuarios conectados

pm [username] [message]: enviar message a username

rm [chatroom] [message]: enviar message a chatroom

d: desconectarse del servidor y cerrar la interfaz



