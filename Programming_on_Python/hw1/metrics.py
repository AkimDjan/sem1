from uuid import UUID
from typing import Sequence


class PeriodActiveUsers:
    GOOD_ACCUMULATION_PERIOD = 1
    _accumulation_period: int
    _unique_users_amount: int
    _last_users_session: dict[UUID:int]

    def __init__(self, accumulation_period: int) -> None:

        """
        Инициализирует объект для подсчета числа уникальных пользователей.

        Args:
            accumulation_period: период времени, для которого необходимо подсчитать
                число уникальных пользователей.

        Raises:
            TypeError, если accumulation_period не может быть округлено и использовано
                для получения целого числа.
            ValueError, если после округления accumulation_period - число, меньшее 1.
        """
        self._last_users_session = dict()
        try:
            int_accumulation_period = round(accumulation_period)
        except TypeError:
            raise TypeError("Accumulation period must be a number: float or integer")
        if int_accumulation_period >= self.GOOD_ACCUMULATION_PERIOD:
            self._accumulation_period = int_accumulation_period
        else:
            raise ValueError("Accumulation period must be bigger or equal than 1")

    def add_active_users_for_curr_day(self, users: Sequence[UUID]) -> None:
        """
        Обновляет метрику на основании данных о посещении ресурса для текущего дня.

        Args:
            users: последовательность UUID пользователей, посетивших ресурс
                в данный день.
        """
        for user in users:
            self._last_users_session[user] = 0
        last_users_copy = dict(self._last_users_session)
        for user in self._last_users_session:
            if self._last_users_session[user] >= self._accumulation_period:
                last_users_copy.pop(user)
            else:
                last_users_copy[user] += 1
        self._last_users_session = dict(last_users_copy)

    @property
    def unique_users_amount(self) -> int:
        """Число уникальных пользователей за последние accumulation_period дней."""
        return len(self._last_users_session)

    @property
    def accumulation_period(self) -> int:
        """Период расчета метрики: accumulation_period."""
        return self._accumulation_period
