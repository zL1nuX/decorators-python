import functools as fc
import time

PASS = '123'


def password_lock(func):
    flag = False

    @fc.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal flag
        if not flag:
            flag = True
            password = input("Введите пароль: ")
            if password == PASS:
                return func(*args, **kwargs)
            else:
                print('В доступе отказано')
        else:
            return func(*args, **kwargs)

    return wrapper


@password_lock
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


start = time.perf_counter()
print(fib(10))
print(fib(11))
print(fib(30))
print(time.perf_counter() - start)
