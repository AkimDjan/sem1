import pytest

# from Generators.second_dot_second_mapper_TOP import mapper
from mapper_2_2 import mapper


result = list(mapper(lambda x, y: x + y, [1, 2], [3], policy="long", fillvalue=0))
assert result == [4, 2]

result = list(mapper(lambda x, y: x + y, [1, 2], [3, 4], policy="short"))
assert result == [4, 6]

with pytest.raises(ValueError):
    list(mapper(lambda x, y: x + y, [1, 2], [3], policy="invalid"))

result = list(mapper(lambda x, y: x + y, [1, 2], [3], policy="long", fillvalue=[0, 1]))
assert result == [4, 3]

result = list(mapper(lambda x, y: x + y, [1, 2], [3], policy="long", fillvalue=0))
assert result == [4, 2]

result = list(
    mapper(
        lambda x, y: x + y,
        [1, 2],
        [3],
        policy="long",
        fillvalue=0
    )
)
assert result == [4, 2]

result = list(
    mapper(
        lambda x, y: x + y,
        [1, 2],
        [3],
        policy="long",
        fillvalue=[5]
    )
)
assert result == [4]


result = list(
    mapper(
        lambda x, y: x + y,
        [1, 2],
        [3],
        policy="long",
        fillvalue=[10, 20]
    )
)
assert result == [4, 22]


with pytest.raises(ValueError):
    list(mapper(lambda x: x, [1, 2], policy="invalid_policy"))


result = list(
    mapper(
        lambda x, y: x * y,
        [1, 2, 3],
        [4, 5],
        policy="short"
    )
)
assert result == [4, 10]



result = list(
    mapper(
        lambda x, y: x * y,
        [1, 2],
        [3],
        policy="long"
    )
) 
print(result)


result = list(
    mapper(
        lambda x, y, z: x + y + z,
        [1],
        [2, 3],
        [4, 5, 6],
        policy="long",
        fillvalue=[10, 20, 30]
    )
)
assert result == [7, 18, 36]


result = list(
    mapper(
        lambda x, y: x + y,
        range(1000),
        range(500),
        policy="short"
    )
)
assert result == [x * 2 for x in range(500)]


result = list(
    mapper(
        lambda x, y: x - y,
        range(1000),
        range(500),
        policy="long",
        fillvalue=10
    )
)
assert result[500:510] == [490, 491, 492, 493, 494, 495, 496, 497, 498, 499]


result = list(
    mapper(
        lambda x, y: x + y,
        [],
        [],
        policy="long",
        fillvalue=0
    )
)
assert result == []


result = list(
    mapper(
        lambda x, y: x + y,
        [1, 2, 3],
        [4, 5],
        policy="long",
        fillvalue=10
    )
)
assert result == [5, 7, 13]


result = list(
    mapper(
        lambda x, y: x + y,
        [1, 2],
        [3],
        policy="long",
        fillvalue=100
    )
)
assert result == [4, 102]


result = list(
    mapper(
        lambda x, y, z: x + y + z,
        [1, 2, 3],
        [4, 5],
        [6, 7, 8],
        policy="short"
    )
)
assert result == [11, 14]


result = list(
    mapper(
        lambda x, y, z: x + y + z,
        [1, 2, 3],
        [4, 5],
        [6],
        policy="long",
        fillvalue=0
    )
)
assert result == [11, 7, 3]



