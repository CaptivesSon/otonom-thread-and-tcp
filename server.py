import socket

server = socket.socket()  # creat socket object
IP = 'localhost'
PORT = 54635  # random but it should be unused

server.bind((IP, PORT))  # it is a tuple
server.listen(1)  # how many people can connect

client, client_address = server.accept()  # accept connection requests
print(client_address)

message = input("Send a message:")

client.send(message.encode())  # sending a message

server.close()