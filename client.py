import socket, config
from autorisation import login, register

def connect(username):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((config.SERVER_IP, config.SERVER_PORT))

        
def autorisation():
    while True:
        print("""\nДобро пожаловать в Vexora\nВыберите действие по номеру ниже\n\n\n[1] - Регистрация\n\n[2] - Вход\n\n""")

        inp = input("[Vexora] > ")

        if inp == "1":
            register.register()

        elif inp == "2":
            username = login.login()
            connect(username)
        else:
            print("Выберите вариант 1 либо 2.")
        

autorisation()

