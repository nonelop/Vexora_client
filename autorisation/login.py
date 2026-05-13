from connection.server_requests.database import check_username


def login():
    while True:
        name = input("Введите логигн: ")
        password = input("Введите пароль: ")

        is_exist = check_username(username=name)

        if is_exist == 1:
            is_password_correct = database.check_password(
                username=name, password=password
            )

            if is_password_correct:
                print("Успешная авторизация.\n")
                return name
            else:
                print("Неправильный пароль. попробуйте ещё раз")
        else:
            print(
                "Пользователя с таким именем не существует. попробуйте еще раз, либо используйте регистрацию"
            )
            break
