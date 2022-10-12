import socket
import threading

LENGTH_MSG = 1024  # bytes
PORT = 1500
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!Disconnect'
# server = '192.168.1.4'
# this mean get the host by name
SERVER = socket.gethostbyname(socket.gethostname())
# print(f"Server: {server}")  # 192.168.1.4
# print(f"Host name: {socket.gethostname()}")  # mbp-macbook

# Binding the port and server
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"New client {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(LENGTH_MSG).decode(FORMAT)
        if msg_length:  # if the message not none
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"{addr} - {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Number of connections are: {threading.activeCount() - 1}")


print("Server is connecting....")
start()
