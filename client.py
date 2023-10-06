import socket

server = socket.socket()  # creat socket object
IP = 'localhost'
PORT = 54635  # random but it should be unused

server.connect((IP, PORT))  # it is a tuple
print("Connection successful")

# sending a message
message = input("Send a message: ")
server.send(message.encode())

server.close()