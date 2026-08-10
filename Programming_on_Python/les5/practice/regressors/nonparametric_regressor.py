from typing import Sequence, Union, Optional
from numbers import Real

from regressors.regressor_abc import RegressorABC


class NonparametricRegressor(RegressorABC):
    NEAREST_LIMIT: int = 1

    _abscissa: Optional[list[Real]]
    _ordinates: Optional[list[Real]]
    _k_nearest_original: int
    _k_nearest: int

    def __init__(self, k_nearest: int = 5) -> None:
        self._k_nearest = round(k_nearest)
        self._k_nearest_original = self._k_nearest

        if self._k_nearest < self.NEAREST_LIMIT:
            raise ValueError("k_nearest must be a natural number")

        self._abscissa = None
        self._ordinates = None

    def fit(self, abscissa: Sequence[Real], ordinates: Sequence[Real]) -> None:
        if not abscissa or not ordinates:
            raise ValueError("sequence must not be empty")

        if len(abscissa) != len(ordinates):
            raise ValueError(f"shape mismatch: {len(abscissa)} != {len(ordinates)}")

        self._abscissa = list(abscissa)
        self._ordinates = list(ordinates)
        self._k_nearest = min(self._k_nearest_original, len(abscissa) - 1)

    def predict(self, abscissa: Union[Real, Sequence[Real]]) -> list:
        if self._abscissa is None or self._ordinates is None:
            raise RuntimeError("fit must be called first")

        if isinstance(abscissa, Real):
            return [self._get_approximation(abscissa)]

        return [
            self._get_approximation(abscissa_i) for abscissa_i in abscissa
        ]

    def _get_approximation(self, abscissa: Real) -> float:
        k_nearest_abscissa = sorted(
            self._abscissa, key=lambda x: abs(x - abscissa)
        )[self._k_nearest]
        window_size = abs(abscissa - k_nearest_abscissa)
        weights = self._get_weights(abscissa, window_size)

        numerator = sum(
            map(lambda tup_: tup_[0] * tup_[1], zip(self._ordinates, weights)),
        )
        return numerator / sum(weights)

    def _get_weights(self, abscissa: Real, window_size: float) -> list[float]:
        weights = []

        for abscissa_i in self._abscissa:
            kernel_arg = abs(abscissa - abscissa_i) / window_size
            weight = 0.75 * (1 - kernel_arg ** 2) if kernel_arg < 1 else 0
            weights.append(weight)

        return weights
