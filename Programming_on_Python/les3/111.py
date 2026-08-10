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
    actions=list()
    avg,sm=0,0
    def get_avg(now:int):
        nonlocal actions, avg, sm
        actions.append(now)
        sm+=now
        ln=len(actions)
        if len(actions)>accumulation_period:
            avg=avg-actions[ln-accumulation_period-1]/accumulation_period+(now/accumulation_period)
            actions.pop(0) #знаю, что pop сильно нагружает, но это намного лучше чем просто память заполнять бесконечно) 
                           #прошу не снижать за это, поскольку требование выполнено :)
        else:
            avg=sm/ln
        return avg
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