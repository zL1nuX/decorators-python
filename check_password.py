PASS = '123'


def password_lock(func):
    def wrapper(*args, **kwargs):
        password = input("Введите пароль: ")
        if password == PASS:
            func(*args, **kwargs)
        else:
            print('В доступе отказано')

    return wrapper


@password_lock
def add(a, b, c=3):
    print(a + b + c)


print(add(1, 2, c=4))
