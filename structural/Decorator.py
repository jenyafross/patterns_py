import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        st = time.perf_counter()
        r = func(*args, **kwargs)
        et = time.perf_counter()
        print('{}: {:.5f}s'.format(func.__name__, et - st))
        return r

    return wrapped


if __name__ == '__main__':
    @timeit
    def wait(s):
        time.sleep(s)
        return f'Wait for {s} seconds'


    def wait_v1(s):
        time.sleep(s)
        return f'Wait for {s} seconds'


    """Декоратор можно использовать как обычную функцию"""
    print(timeit(wait_v1)(3))
    print(wait(2))
    """Благодаря конструкции @wraps(func) в мы сохраняем метаданные оригинальной функции, например __name__"""
    print(wait.__name__)
