import socket
import sys


def create_socket():

    try:
        global host
        global port
        global s

        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Error creating socket: " + str(msg))


def bind_socket(call_count):
    try:
        print("Binding the socket to " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Error in binding the socket: " + str(msg) + "\nRetrying... ")
        if call_count > 0:
            bind_socket(call_count - 1)


def accept_socket():
    try:
        conn, address = s.accept()
        print("Connection has been established... IP: " + address[0] + " PORT: " + str(address[1]))
        send_commands(conn)
        conn.close()
    except socket.error as msg:
        print(msg)


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')
            print(client_response, end='')


if __name__ == '__main__':
    create_socket()
    bind_socket(call_count=3)
    accept_socket()




