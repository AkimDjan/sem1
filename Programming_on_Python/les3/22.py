#тайм для времени, импортируем ее и есть функция time, текущее время в секундах, параметризованный декоратор
def is_floats_eq(lhs: float, rhs: float, eps: float = 1e-6) -> bool:
    """
    Сравнивает числа с плавающей точкой на равенство с заданной точностью.

    Args:
        lhs: левый аргумент сравнения.
        rhs: правый аргумент сравнения.
        eps: точность. По умолчанию сравнение происходит с точностью до 6 знаков после запятой.

    Returns:
        Булево значение. True, если числа равны, False - иначе.
    """
    return abs(lhs - rhs) < eps

from functools import wraps
import time

from typing import Callable, TypeVar
T = TypeVar("T")


def collect_statistic(
    statistics: dict[str, list[float, int]]
) -> Callable[[T], T]:
    def _collect(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            if func.__name__ not in statistics:
                statistics[func.__name__] = [0, 0]
            statistics[func.__name__][1] += 1
            runtime_start = time.time()
            res = func(*args, **kwargs)
            runtime = time.time() - runtime_start
            preavg = statistics[func.__name__][0]
            count = statistics[func.__name__][1]
            statistics[func.__name__][0]  = (preavg * (count-1) + runtime) / count
            return res
        return _wrapper    
    return _collect
    


statistics: list[str, list[float, int]] = {}

@collect_statistic(statistics)
def func1() -> None:
    time.sleep(2)


@collect_statistic(statistics)
def func2() -> None:
    time.sleep(1)

for _ in range(3):
    func1()

for i in range(6):
    func2()



print(func2.__code__.co_freevars)
print(func2.__closure__)

print(*func2.__closure__)

for i in func2.__closure__:
    print(i.cell_contents)