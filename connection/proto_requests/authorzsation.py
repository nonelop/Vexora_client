import json
from connection.server_connection import connect_to_server, disconnect_to_server


def write_new_user(data: tuple):
    sock = connect_to_server()

    if sock != 0:
        request = {
            "method": "authorization",
            "operation": "register_new_user",
            "data": {
                "username": data[0],
            },
        }

        json_request = json.dumps(request)
        byte_request = json_request.encode(encoding="utf-8")

        sock.sendall(byte_request)

        operation_status = sock.recv(512).decode()
        operation_status_str = json.loads(operation_status)

        disconnect_to_server(sock)

        return operation_status_str

    else:
        return 0


def check_username(username: str):
    sock = connect_to_server()

    if sock != 0:
        request = {
            "method": "authorization",
            "operation": "check_user_username",
            "data": {
                "username": username,
            },
        }

        json_request = json.dumps(request)
        byte_request = json_request.encode(encoding="utf-8")

        sock.sendall(byte_request)

        operation_status = sock.recv(512).decode()
        operation_status_str = json.loads(operation_status)

        disconnect_to_server(sock)

        return operation_status_str["data"][0]

    else:
        return 0
