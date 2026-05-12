import socket
from autorisation import login, register

while True:
    print("Добро пожаловать в Babuin!\n\n\n[1] Регистрация\n\n[2] Вход\n")
    inp = input("Выберите действие: ")

    try:
        inp = int(inp)
    except:
        print("Пожалуйста, введите число.")

    if inp == 1:
        register.register()
    elif inp == 2:
        name = login.login()
        if name:
            break
    else:
        print("Выберите вариант 1 либо 2")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("192.168.2.5", 5050))

    while True:
        inp = input("Сообщение на сервер: ")
        message = f"{name}: {inp}"
        sock.send(message.encode())
