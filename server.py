import socket
import sys


def create_socket():

    try:
        global host
        global port
        global s

        host = ""
        port = 31377
        s = socket.socket()
    except socket.error as msg:
        print("Error creating socket: " + str(msg))




def bind_socket(call_count):



    try:

        global host
        global port
        global s

        print("Binding the socket to " + str(port))

        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Error in binding the socket: " + str(msg) + "\nRetrying... ")
        if (call_count > 0):
            bind_socket(call_count - 1)


if __name__ == '__main__':
    create_socket()
    bind_socket(call_count=3)




