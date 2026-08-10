import unittest
from cache import lru_cache

class TestLRUCache(unittest.TestCase):

    def test_basic_caching(self):
        @lru_cache(2)
        def add(x, y):
            return x + y

        # Первые два вызова добавляются в кэш
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 3), 5)

        # Проверка, что результат повторного вызова берется из кэша
        self.assertEqual(add(1, 2), 3)

    def test_cache_eviction(self):
        @lru_cache(2)
        def multiply(x, y):
            return x * y

        # Добавляем два значения
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(3, 4), 12)

        # Вызов третьего значения должен вытеснить старое (2, 3)
        self.assertEqual(multiply(4, 5), 20)

        # Кэш должен удалить первый элемент, и снова вычислить (2, 3)
        self.assertEqual(multiply(2, 3), 6)

    def test_cache_order(self):
        @lru_cache(3)
        def power(x, y):
            return x ** y

        # Добавляем три значения
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(power(4, 1), 4)

        # Проверяем, что вызов power(2, 3) не удаляется
        self.assertEqual(power(2, 3), 8)

        # Вызов нового значения должен вытеснить наименее используемое
        self.assertEqual(power(5, 2), 25)

        # Проверяем, что кэш удалил значение power(3, 2)
        self.assertEqual(power(3, 2), 9)

    def test_incorrect_capacity_type(self):
        with self.assertRaises(TypeError):
            @lru_cache("invalid")
            def dummy_func(x):
                return x

    def test_capacity_less_than_one(self):
        with self.assertRaises(ValueError):
            @lru_cache(0)
            def dummy_func(x):
                return x

    def test_cache_with_kwargs(self):
        @lru_cache(2)
        def concat_strings(a, b, c="default"):
            return f"{a}-{b}-{c}"

        self.assertEqual(concat_strings("hello", "world"), "hello-world-default")
        self.assertEqual(concat_strings("foo", "bar", c="baz"), "foo-bar-baz")

        # Повторный вызов должен быть из кэша
        self.assertEqual(concat_strings("foo", "bar", c="baz"), "foo-bar-baz")

        # Вызов нового значения должен вытеснить первое
        self.assertEqual(concat_strings("new", "value"), "new-value-default")

    def test_cache_with_large_capacity(self):
        @lru_cache(1000)
        def identity(x):
            return x

        for i in range(1000):
            self.assertEqual(identity(i), i)

        # Проверим, что при большом capacity всё ещё работает корректно
        self.assertEqual(identity(1001), 1001)
        self.assertEqual(identity(1), 1)

if __name__ == "__main__":
    unittest.main()
