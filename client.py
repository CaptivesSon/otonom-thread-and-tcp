import socket

server = socket.socket()  # creat socket object
IP = 'localhost'
PORT = 54635  # random but it should be unused

server.connect((IP,PORT))  # it is a tuple
print("Connection successful")

message = server.recv(1024)  # taking the messages
print(message.decode())

server.close()