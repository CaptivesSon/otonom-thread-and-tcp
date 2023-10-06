import socket
import threading
import time

server = socket.socket()  # creat socket object
IP = 'localhost'
PORT = 54635  # random but it should be unused

server.connect((IP, PORT))  # it is a tuple
print("Connection successful")


# message count
def get_count():
    x = int(input("How many messages do you want to send?: "))
    return x


# taking messages from user
def get_messages(a):
    b = []
    for i in range(a):
        b.append(input("Send a message: "))
    return b


# threading
class ThreadingDownloader(threading.Thread):

    def _init_(self):
        super().__init__()  # inheritance
        self.messages_array = []  # empty list for messages

    def run(self):

        message_count = get_count()  # request message count
        messages_3 = get_messages(message_count)  # request messages
        for message in messages_3:
            self.messages_array.append(message)  # appending the messages to the array
        return self.messages_array


def get_data_threading():
    st = time.time()  # start time
    threads = []  # empty list for threads

    t = ThreadingDownloader()
    t.start()
    threads.append(t)

    for t in threads:
        t.join()
        print(t)
        for i in t.messages_array:
            server.send(i.encode())

    et = time.time()  # finish time
    elapsed_time = et - st  # elapsed time
    print(f"Execution time: {elapsed_time}")


get_data_threading()

server.close()