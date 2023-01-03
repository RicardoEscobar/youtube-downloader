import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        seconds = end - start
        print(f"{func.__name__} took {seconds:.2f} seconds")
        return result
    return wrapper
