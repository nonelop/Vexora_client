from connection.server_requests.database import check_username


def login():
    while True:
        name = input("Введите логигн: ")

        is_exist = check_username(username=name)

        if is_exist == True:
            print("Успешная авторизация.\n")
            return name

        else:
            print(
                "Пользователя с таким именем не существует. попробуйте еще раз, либо используйте регистрацию"
            )
            break
