#import database


def login():
    while True:
        name = input("Введите логигн: ")
        password = input("Введите пароль: ")

        is_exist = database.check_user(username=name)

        if is_exist:
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
