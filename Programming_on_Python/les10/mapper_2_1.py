from typing import Generator, Iterable, Callable

def mapper(func: Callable, *iters: Iterable) -> Generator:
    if bool(iters)==0:
        raise ValueError("Iterable object cant be empty")
    try:
        iters = zip(*iters) #создаем кортежи полеменетно из итерируемых объектов
    except:
        TypeError("mapper's arguments after first must be iterable")
    
    for i in iters:
        yield func(*i) #распакоука кортежей, подача в функцию
    
    
