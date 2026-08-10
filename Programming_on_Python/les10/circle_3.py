from typing import Generator, Iterable

def circle(iterobj: Iterable) -> Generator:
    iterobj = iter(iterobj)
    try:
        iterobj = list(iterobj)
        N = len(iterobj)
        i = 0
        if N == 0:
            raise ValueError("We cant iterate on 0-lentgh iterable object")
        while True:
            yield iterobj[i % N]
            i += 1
    except TypeError:
        while True:
            try:
                yield next(iterobj)
            except StopIteration:
                iterobj = iter(iterobj)


