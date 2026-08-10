import pytest

from mapper_2_1 import mapper

result = list(mapper(lambda x: x * 2, range(5)))
assert result == [0, 2, 4, 6, 8]

result = list(mapper(lambda x, y: x + y, [1, 2], [3, 4]))
assert result == [4, 6]

result = list(mapper(lambda x, y: x + y, [1, 2], [3]))
assert result == [4]

result = list(mapper(lambda x, y: x + y, [], [1, 2]))
assert result == []

with pytest.raises(ValueError):
    list(mapper(lambda x: x))

result = mapper(lambda x: x * 2, range(3))
assert iter(result) is not list

result = list(mapper(lambda x: x * x, range(1000)))
assert result == [i * i for i in range(1000)]

with pytest.raises(TypeError):
    list(mapper(None, range(5)))

with pytest.raises(TypeError):
    list(mapper(5, range(5)))

result = list(mapper(lambda x, y: x - y, range(10), range(5)))
assert result == [i - i for i in range(5)]


result = list(mapper(lambda x, y: str(x) + y, [1, 2], ["a", "b"]))
assert result == ["1a", "2b"]

result = list(mapper(lambda x, y: x + y, [[1], [2]], [[3], [4]]))
assert result == [[1, 3], [2, 4]]

with pytest.raises(TypeError):
    list(mapper())

result = list(mapper(lambda x: x**2, [1, 2, 3, 4]))
assert result == [1, 4, 9, 16]

result = list(mapper(lambda x, y, z: x + y + z, [1, 2], [3, 4, 5], [6]))
assert result == [10]

result = list(mapper(lambda x, y: x + len(y), [1, 2], ["a", "bc"]))
assert result == [2, 4]

result = list(mapper(lambda x, y: x + y, [], []))
assert result == []

with pytest.raises(TypeError):
    list(mapper(lambda x, y: x + y, [1, 2], 3))

def faulty_function(x, y):
    if x == 1:
        raise ValueError("Test exception")
    return x + y

with pytest.raises(ValueError):
    list(mapper(faulty_function, [1, 2], [3, 4]))

result = list(
    mapper(
        lambda *args: sum(args),
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
    )
)
assert result == [16, 20]

with pytest.raises(TypeError):
    list(mapper(123, [1, 2], [3, 4]))

with pytest.raises(TypeError):
    list(mapper(lambda x: x, None))

result = list(mapper(str.upper, ["a", "b", "c"]))
assert result == ["A", "B", "C"]

result = list(mapper(lambda x, y: x + y, [1, 2, 3], []))
assert result == []

result = list(mapper(lambda x, y: x * y, [1, 2, 3], [4, 5]))
assert result == [4, 10]

result = list(mapper(lambda x, y: x * y, [1, 2, 3], [4, 5]))
assert result == [4, 10]

result = list(mapper(lambda x, y: x + y, ["a", "b", "c"], ["x", "y"]))
assert result == ["ax", "by"]

result = list(mapper(lambda x, y, z: x + y + z, [1, 2], [3, 4], [5, 6]))
assert result == [9, 12]

result = list(mapper(lambda x: x * 2, [1, 2, 3]))
assert result == [2, 4, 6]

result = list(mapper(lambda x: x * 2, []))
assert result == []

result = list(mapper(lambda x, y: x + y, [1, 2, 3], [4]))
assert result == [5]

with pytest.raises(TypeError):
    list(mapper())

#result = list(mapper(lambda x, y: x + y, [1, 2], [3, 4], [5, 6]))
#assert result == [4, 6]


result = list(mapper(lambda x, y: f"{x}{y}", [1, 2], ["a", "b"]))
assert result == ["1a", "2b"]

result = list(mapper(lambda x: x * 2, range(1000)))
assert result == [i * 2 for i in range(1000)]

with pytest.raises(TypeError):
    list(mapper(5, range(5)))

result = list(mapper(lambda x, y, z: x + y + z, [1], [2], [3]))
assert result == [6]

result = list(mapper(lambda x, y: x if y is None else x + y, [1, 2, 3], [None, 4, None]))
assert result == [1, 6, 3]

result = list(mapper(lambda x, y: x and y, [True, False, True], [False, True, True]))
assert result == [False, False, True]

result = list(mapper(lambda x, y: [a + b for a, b in zip(x, y)], [[1, 2], [3, 4]], [[5, 6], [7, 8]]))
assert result == [[6, 8], [10, 12]]

result = list(mapper(lambda x, y: x + y, [1, 2], (3, 4)))
assert result == [4, 6]

with pytest.raises(TypeError):
    list(mapper(None, [1, 2, 3]))


