from typing import Sequence, Union
from numbers import Real

from regressors.regressor_abc import RegressorABC


class RegressorLSM(RegressorABC):
    _abscissa: list[Real]
    _ordinates: list[Real]
    _coef_a: Real
    _coef_b: Real
    
    def __init__(self) -> None:
        self._abscissa = []
        self._ordinates = []
        self._coef_a = 0.0  #считая, что y=bx+a
        self._coef_b = 0.0

    def fit(self, abscissa: Sequence[Real], ordinates: Sequence[Real]) -> None:
        if not abscissa or not ordinates:
            raise ValueError("sequence must not be empty")

        if len(abscissa) != len(ordinates):
            raise ValueError(f"shape mismatch: {len(abscissa)} != {len(ordinates)}")
        
        self._abscissa = list(abscissa)
        self._ordinates = list(ordinates)

        y_avg=self._get_avg(self._ordinates)
        x_avg=self._get_avg(self._abscissa)
        xy_avg=self._get_avg([x*y for x,y in zip(self._abscissa,self._ordinates)])
        xx_avg=self._get_avg([x*x for x in self._abscissa])

        self._coef_b=((xy_avg - y_avg* x_avg) / (xx_avg - x_avg**2))#формула нахождения коэф. b
        self._coef_a=(y_avg-self._coef_b*x_avg)
        

    def predict(self, abscissa: Union[Real, Sequence[Real]]) -> list:
        if self._abscissa is None or self._ordinates is None:
            raise RuntimeError("fit must be called first")
        
        if isinstance(abscissa, Real):
            return [self._get_approximation(abscissa)]  
        
        return [self._get_approximation(abscissa_i) for abscissa_i in abscissa]

    def _get_approximation(self, abscissa: Real) -> float:
        return self._coef_b*abscissa+self._coef_a

    def _get_avg(self,values:list[Real]) -> float:
        return sum(values)/len(values)

