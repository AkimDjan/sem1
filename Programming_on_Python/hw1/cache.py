from typing import (
    Callable,
    TypeVar,
)
from functools import wraps


T = TypeVar("T")


def lru_cache(capacity: int) -> Callable[[T], T]:
    """
    Параметризованный декоратор для реализации LRU-кеширования.

    arguments:
        capacity: целое число, максимальный возможный размер кеша.

    Returns:
        Декоратор для непосредственного использования.

    Raises:
        TypeError, если capacity не может быть округлено и использовано
            для получения целого числа.
        ValueError, если после округления capacity - число, меньшее 1.
    """
    GOOD_CAPACITY = 1
    try:
        int_capacity = round(capacity)
    except TypeError:
        raise TypeError("Capacity must be a number: float or integer")
    if int_capacity < GOOD_CAPACITY:
        raise ValueError("Capacity must be bigger or equal than 1")
    cache = dict()

    def fun(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            argument = tuple([args, tuple(sorted(kwargs.items()))])
            if (argument in cache):
                res_intermediate = cache[argument]
                del cache[argument]
                cache[argument] = res_intermediate
                return cache[argument]
            else:
                res = func(*args, **kwargs)
            if len(cache) >= int_capacity:
                del cache[tuple(cache.keys())[0]]
            cache[argument] = res
            return res
        return wrapper
    return fun
