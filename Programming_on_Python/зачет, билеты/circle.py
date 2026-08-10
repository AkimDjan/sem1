from collections.abc import Iterable
from typing import Generator


def circle(iterable: Iterable) -> Generator:
    if not isinstance(iterable, Iterable):
        TypeError("iterable должен быть итерируем")

    save_values = []
    for value in iterable:
        yield value
        save_values.append(value)
    
    if not len(save_values):
        return

    while True:
        yield from save_values