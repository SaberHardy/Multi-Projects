import socket

HEADER = 64
PORT = 1500
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.4"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send_message(message):
    # convert message to bytes objects
    message = message.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    print(f"send length= {send_length}")
    client.send(send_length)
    client.send(message)
    print(f"Client Sent==> {client.recv(2048).decode(FORMAT)}")


send_message("Hello World!")
send_message(DISCONNECT_MESSAGE)
