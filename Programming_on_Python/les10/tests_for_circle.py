import pytest

from circle_3 import circle


circle_gen = circle("abc")
result = [next(circle_gen) for _ in range(6)]
assert result == ["a", "b", "c", "a", "b", "c"]


circle_gen = circle("a")
result = [next(circle_gen) for _ in range(5)]
assert result == ["a", "a", "a", "a", "a"]

with pytest.raises(ValueError):
    next(circle(""))


data = range(100)
circle_gen = circle(data)
result = [next(circle_gen) for _ in range(105)]
assert result == list(data) + list(data[:5])

data = "ab"
circle_gen = circle(data)
result = [next(circle_gen) for _ in range(10)]
assert result == ["a", "b"] * 5





gen = circle("abc")
assert next(gen) == "a"
assert next(gen) == "b"
assert next(gen) == "c"
assert next(gen) == "a"
assert next(gen) == "b"


gen = circle([1, 2, 3])
assert next(gen) == 1
assert next(gen) == 2
assert next(gen) == 3
assert next(gen) == 1
assert next(gen) == 2


gen = circle((10, 20, 30))
assert next(gen) == 10
assert next(gen) == 20
assert next(gen) == 30
assert next(gen) == 10


gen = circle([42])
assert next(gen) == 42
assert next(gen) == 42
assert next(gen) == 42


with pytest.raises(ValueError):
    gen = circle([])
    next(gen)


gen_input = (x**2 for x in range(3))
gen = circle(gen_input)
assert next(gen) == 0
assert next(gen) == 1
assert next(gen) == 4


gen = circle(range(1, 1001))
for i in range(1, 1001):
    assert next(gen) == i
assert next(gen) == 1  # Cycle restarts


with pytest.raises(TypeError):
    gen = circle(42)
    next(gen)


lst = [1, 2, 3]
gen = circle(lst)
assert next(gen) == 1
assert next(gen) == 2
assert next(gen) == 3


gen = circle("xy")
assert [next(gen) for _ in range(10)] == ["x", "y", "x", "y", "x", "y", "x", "y", "x", "y"]


gen = circle([0, 1])
for _ in range(1000):
    assert next(gen) in [0, 1]


class Custom:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Custom({self.name})"

objects = [Custom("A"), Custom("B")]
gen = circle(objects)
assert repr(next(gen)) == "Custom(A)"
assert repr(next(gen)) == "Custom(B)"
assert repr(next(gen)) == "Custom(A)"


iterable = iter([1, 2, 3])
gen = circle(iterable)
assert next(gen) == 1
assert next(gen) == 2
assert next(gen) == 3


gen = circle([True, False])
assert next(gen) is True
assert next(gen) is False
assert next(gen) is True

gen = circle([1 + 2j, 3 + 4j])
assert next(gen) == 1 + 2j
assert next(gen) == 3 + 4j
assert next(gen) == 1 + 2j

