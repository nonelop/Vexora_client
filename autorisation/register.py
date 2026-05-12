from connection.server_requests.database import write_new_user


def register():
    while True:
        print("\nРегистрация в Babuin\n")
        name = input("Введите логигн: ")
        password = input("Придумайте пароль: ")

        # is_exist = database.check_user(username=name)

        # if is_exist:
        #     print("Пользователь с таким именем уже сущетсвует.")
        # else:
        print(write_new_user(data=(name, password)))
        print("Запись успешно созданна! войдите в нее через Вход")
        break
