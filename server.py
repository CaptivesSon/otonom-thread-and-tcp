import socket

server = socket.socket()  # creat socket object
IP = 'localhost'
PORT = 54635  # random but it should be unused

server.bind((IP, PORT))  # it is a tuple
server.listen(1)  # how many people can connect


# accept connection requests
client, client_address = server.accept()
print(client_address)


message = client.recv(1024)  # taking the messages
print(message.decode())

server.close()