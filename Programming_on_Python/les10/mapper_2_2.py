from typing import Generator, Iterable, Callable, Any
from itertools import chain, zip_longest

def fullfill(iters: tuple[Iterable],fillvalue: Iterable[Any]) -> tuple[Iterable]:
    maxlen = len(max(iters, key = len))
    new_iters = tuple()
    for i in range(len(iters)):
        new_iter = list(iters[i])
        while len(new_iter) < maxlen:
            new_iter.append(fillvalue[i])
        new_iters = new_iters + (new_iter, )
    return new_iters
            
def mapper(func: Callable, *iters: Iterable, policy = "short", fillvalue = None) -> Generator:
    if policy == "short":
        try:
            iters = zip(*iters)
            for i in iters:
                yield func(*i)
        except:
            TypeError("mapper's arguments after first must be iterable")
    elif policy == "long":
        try:
            if not isinstance(fillvalue, Iterable) or (isinstance(fillvalue, Iterable) and len(fillvalue) != len(iters)):
                iters = zip_longest(*iters,fillvalue=fillvalue)
            elif len(fillvalue) == len(iters):
                iters = zip(*fullfill(iters,fillvalue))
            for i in iters:
                yield func(*i)  
        except:
            TypeError("mapper's arguments after first and before policy and fillvalue must be iterable")
    else:
        raise ValueError('Policy argument must be only "short" and "long" ')




