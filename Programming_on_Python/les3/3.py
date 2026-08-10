from functools import wraps
import time
from typing import Callable, TypeVar
T = TypeVar("T")


def retry(retries: int = 3, timeout: float = 1) -> Callable[[T], T]:
    def again(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    res=func(*args,**kwargs)
                except Exception:
                    time.sleep(timeout)
                else:
                    return res
            else:
                raise Exception
        return wrapper
    return again

def raiser_factory(stop_on: int = 2) -> Callable:
    call_counter = 0

    def raiser(*args, **kwargs) -> None:
        nonlocal call_counter

        if call_counter != 0 and call_counter % stop_on == 0:
            return
        
        call_counter += 1
        raise Exception

    return raiser

# первый пример
raiser = retry()(raiser_factory())
raiser()

# второй пример
raiser = retry()(raiser_factory(stop_on=4))
try:
    raiser()
    was_raised = False

except Exception:
    was_raised = True

assert was_raised