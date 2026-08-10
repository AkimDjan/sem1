from decimal import Decimal, getcontext
from types import TracebackType
from typing import Optional

class Precision:
    _prev_precision: int
    _precision: int

    def __init__(self, precision: int) -> None:
        GOOD_PRECISION_LEN = 1
        try:
            int_precision = round(precision)
        except TypeError:
            raise TypeError("Precision must be a number: float or integer")
        if int_precision < GOOD_PRECISION_LEN:
            raise ValueError("Precision must be bigger or equal than 1")
        self._precision=int_precision
    
    def __enter__(self) -> None:
        self._prev_precision=getcontext().prec
        getcontext().prec=self._precision
    
    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        getcontext().prec=self._prev_precision


precision = 5

with Precision(precision):
    assert getcontext().prec == precision
    print(Decimal("1") / Decimal("3"))



