from typing import Generator
from numbers import Real

def range_float(**kwargs) -> Generator:
    stop = kwargs["stop"]
    start = kwargs.get("start", 0.0)
    step = kwargs.get("step", 1.0)
    for arg in (start, stop, step):
        if not isinstance(arg, Real):
            raise TypeError("start,stop,step must be only real numbers")
    if step==0 or (start - stop) * step > 0:
        return []
    if stop > start:
        i = start
        while i < stop:
            yield i
            i += step
    else:
        i = start
        while i > stop:
            yield i
            i += step

    
for i in range_float(stop=10):
    print(i)

"""k = 1 #коэффициент домножения для start
    l = 1 # коэффициент домножения для step
    if start % 1 > 0:
        k = 1 / start
        start, stop, step = map(lambda x : k * x, (start, stop, step))
    if step % 1 > 0:
        l = 1 / step
        start, stop, step = map(lambda x : l * x, (start, stop, step))
    start, stop, step = map(int, (start, stop, step))
    
    for i in range(start, stop, step):
        yield float(i / (k * l)) #деление на коэффициенты"""