from typing import Callable

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




def make_averager(accumulation_period: int) -> Callable[[float], float]:
    dohodubitok=list()
    sm=0
    def get_avg(now:int):
        dohodubitok+=[now]
        sm+=now
        if len(dohodubitok)>=accumulation_period:
            dohodubitok.pop(0)
        return sum(dohodubitok)/len(dohodubitok)
    return get_avg

#первый пример

get_avg = make_averager(2)

assert is_floats_eq(get_avg(1), 1)
assert is_floats_eq(get_avg(2), 1.5)
assert is_floats_eq(get_avg(3), 2.5) 
assert is_floats_eq(get_avg(-3), 0)
assert is_floats_eq(get_avg(5), 1)
assert is_floats_eq(get_avg(5), 5)

# второй пример
get_avg = make_averager(5)

assert is_floats_eq(get_avg(1), 1)
assert is_floats_eq(get_avg(2), 1.5)
assert is_floats_eq(get_avg(3), 2)
assert is_floats_eq(get_avg(4), 2.5)
assert is_floats_eq(get_avg(5), 3)
assert is_floats_eq(get_avg(-5), 1.8)
assert is_floats_eq(get_avg(-7), 0)
assert is_floats_eq(get_avg(-2), -1)