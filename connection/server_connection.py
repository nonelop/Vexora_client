import socket, config


def connect_to_server():

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((config.SERVER_IP, config.SERVER_PORT))

        return sock

    except:
        return 0


def disconnect_to_server(sock: socket.socket):

    sock.close()
