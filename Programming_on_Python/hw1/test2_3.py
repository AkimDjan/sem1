from cache import lru_cache
import time

@lru_cache(capacity=5)
def f(x: int) -> int:
    if x < 3:
        return x

    return f(x - 2) + f(x - 1) + f(x - 3) + f(x - 4) + f(x - 5)

time_started = time.time()
print(f(25))
print(time.time() - time_started)
