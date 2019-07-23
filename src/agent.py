import socket
import sys

server_port = 5070
server_name = "127.0.0.1"
server_address = (server_name, server_port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        while True:
            data = connection.recv(1024)
            if data:
                msg = data.strip()
                print(msg)
                connection.sendall(msg)
            else:
                break
    finally:
        connection.close()
