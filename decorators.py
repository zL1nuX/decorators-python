import time
import functools as fc

"""redefinition of print"""
print_ = print
print = lambda *args: print_(*list(map(str.upper, args)))
print(input())


def time_measure(func):
    """time measure decorator"""
    @fc.wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        res = func(*args, **kwargs)
        t = time.perf_counter() - t0
        print(t)
        return res

    return wrapper


@time_measure
def kaif(a, b, c=7):
    k = 0
    for i in range(a):
        for x in range(b):
            for y in range(c):
                k += 1
    return k


print(kaif(int(input()), int(input())))



