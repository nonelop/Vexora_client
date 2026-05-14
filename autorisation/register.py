from connection.proto_requests.authorzsation import write_new_user, check_username


def register():
    while True:
        print("\nРегистрация в Vexora\n")
        name = input("Введите логигн: ")

        is_exist = check_username(username=name)
        print(is_exist)

        if is_exist:
            print("Пользователь с таким именем уже сущетсвует.")
        else:
            print(write_new_user(data=(name,)))
            print("Запись успешно созданна! войдите в нее через Вход")
            break
