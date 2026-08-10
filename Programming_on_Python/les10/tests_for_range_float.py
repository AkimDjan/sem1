import pytest

from range_float_1 import range_float
"""
Тесты для задачи 1. 

range_float
"""

result = list(range_float(stop=3))
assert result == [0.0, 1.0, 2.0]

result = list(range_float(start=1, stop=4))
assert result == [1.0, 2.0, 3.0]


result = list(range_float(start=0.5, stop=3, step=0.5))
assert result == [0.5, 1.0, 1.5, 2.0, 2.5]


result = list(range_float(start=0, stop=10, step=3))
assert result == [0.0, 3.0, 6.0, 9.0]


result = list(range_float(start=5, stop=0, step=-1))
assert result == [5.0, 4.0, 3.0, 2.0, 1.0]


result = list(range_float(start=0, stop=1, step=0.1))
print(result) #== [i / 10 for i in range(10)]


with pytest.raises(ValueError):
    list(range_float(start=0, stop=1, step=0))


result = list(range_float(start=1, stop=1))
assert result == []


result = list(range_float(start=5, stop=1, step=-1))
assert result == [5.0, 4.0, 3.0, 2.0]


result = list(range_float(start=0, stop=100000, step=10000))
assert result == [i * 10000.0 for i in range(10)]


result = list(range_float(stop=2))
assert result == [0.0, 1.0]


result = list(range_float(start=0.5, stop=2, step=0.5))
assert result == [0.5, 1.0, 1.5]


result = list(range_float(start=2, stop=0, step=-0.5))
assert result == [2.0, 1.5, 1.0, 0.5]


result = list(range_float(start=5, stop=2, step=-1))
assert result == [5.0, 4.0, 3.0]


result = list(range_float(start=0, stop=1.9, step=0.5))
assert result == [0.0, 0.5, 1.0, 1.5]


with pytest.raises(ValueError):
    list(range_float(start=0, stop=1, step=0))


result = list(range_float(start=1e6, stop=1e6 + 3, step=1))
assert result == [1e6, 1e6 + 1, 1e6 + 2]


result = list(range_float(start=0, stop=0.002, step=0.001))
assert result == [0.0, 0.001]


result = list(range_float(start=1.5, stop=1.5, step=0.1))
assert result == []


result = list(range_float(start=1.5, stop=1.5, step=-0.1))
assert result == []


result = list(range_float(start=0, stop=1e-6, step=1e-7))
assert len(result) == 10
assert result[0] == 0.0
assert result[-1] == 9e-7


result = list(range_float(start=-1, stop=1, step=0.5))
assert result == [-1.0, -0.5, 0.0, 0.5]


result = list(range_float(start=0, stop=10, step=4))
assert result == [0.0, 4.0, 8.0]




result = list(range_float(5, start=0, step=1))
assert result == [0, 1, 2, 3, 4]


result = list(range_float(1, start=5, step=-1))
assert result == [5, 4, 3, 2]


result = list(range_float(1.5, start=0, step=0.3))
print(result) #== [0, 0.3, 0.6, 0.9, 1.2]


result = list(range_float(-1.5, start=0, step=-0.5))
assert result == [0, -0.5, -1.0]

# Тесты на граничные значения

result = list(range_float(1, start=0, step=0.5))
assert result == [0, 0.5]


result = list(range_float(10, start=0, step=20))
assert result == [0]

# Тесты на ошибки

with pytest.raises(ValueError):
    list(range_float(5, start=0, step=0))


with pytest.raises(ValueError):
    list(range_float(1, start=5, step=1))


with pytest.raises(ValueError):
    list(range_float(5, start=0, step=-1))



result = list(range_float(1e6, start=1e5, step=1e5))
assert result == [1e5, 2e5, 3e5, 4e5, 5e5, 6e5, 7e5, 8e5, 9e5]


result = list(range_float(-1e6, start=-1e5, step=-1e5))
assert result == [-1e5, -2e5, -3e5, -4e5, -5e5, -6e5, -7e5, -8e5, -9e5]

# Тесты на пограничные случаи

result = list(range_float(1, start=0, step=2))
assert result == [0]


result = list(range_float(0, start=1, step=-2))
assert result == [1]


result = list(range_float(1, start=0, step=1))
assert result == [0]

# Тесты на очень малые значения

result = list(range_float(1e-5, start=0, step=1e-6))
assert len(result) == 10  # Шаг попадает ровно 10 раз
assert result[0] == 0
assert result[-1] == 9e-6

