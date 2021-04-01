import functools as fc
import time


def cache(func):
    """Кэш предыдущих вызовов функций"""
    @fc.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]

    wrapper.cache = dict()
    return wrapper


# @fc.lru_cache(maxsize=32)
@cache
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


t0 = time.perf_counter()
print(t0)
print(fib(100))
print(time.perf_counter() - t0)
