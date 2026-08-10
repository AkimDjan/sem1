from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def api_computable_exceptions(
        exception_mapping: dict[type[Exception], type[Exception]]
        ) -> Callable[[T], T]:
    def fun(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as exc:
                if type(exc) in exception_mapping:
                    raise exception_mapping[type(exc)] from None
                else:
                    raise exc from None
            
        return wrapper
    return fun


class UnsupportedValueError(Exception):
    pass


class NonExistedKeyError(Exception):
    pass


exception_mapping = {
    ValueError: UnsupportedValueError,
    KeyError: NonExistedKeyError,
}


@api_computable_exceptions(exception_mapping)
def raise_value_error() -> None:
    raise ValueError


@api_computable_exceptions(exception_mapping)
def raise_key_error() -> None:
    raise KeyError


@api_computable_exceptions(exception_mapping)
def raise_exception() -> None:
    raise Exception


try:
    raise_value_error()
    assert False
except UnsupportedValueError:
    pass

try:
    raise_key_error()
    assert False
except NonExistedKeyError:
    pass

try:
    raise_exception()
except Exception as exc:
    assert isinstance(exc, Exception)
    