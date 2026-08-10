import unittest
from math import isclose, sqrt, pi

from vector2d import Vector2D


class TestVector2D(unittest.TestCase):
    def test_initialization(self):
        v1 = Vector2D()
        self.assertEqual(v1.abscissa, 0.0)
        self.assertEqual(v1.ordinate, 0.0)

        v2 = Vector2D(3, 4)
        self.assertEqual(v2.abscissa, 3.0)
        self.assertEqual(v2.ordinate, 4.0)

        with self.assertRaises(AttributeError):
            v2.abscissa = 10

    def test_str_representation(self):
        v = Vector2D(3, 4)
        self.assertEqual(str(v), "Vector2D(abscissa=3, ordinate=4)")

    def test_equality(self):
        v1 = Vector2D(1, 2)
        v2 = Vector2D(1, 2)
        v3 = Vector2D(2, 3)
        self.assertTrue(v1 == v2)
        self.assertFalse(v1 == v3)
        self.assertTrue(v1 != v3)

    def test_ordering(self):
        v1 = Vector2D(1, 1)
        v2 = Vector2D(1, 2)
        v3 = Vector2D(2, 1)
        self.assertTrue(v1 < v2)
        self.assertTrue(v1 <= v2)
        self.assertTrue(v3 >= v2)

    def test_abs(self):
        v = Vector2D(3, 4)
        self.assertTrue(isclose(abs(v), 5.0))

    def test_bool(self):
        v1 = Vector2D()
        v2 = Vector2D(1, 1)
        self.assertFalse(bool(v1))
        self.assertTrue(bool(v2))

    def test_multiplication(self):
        v = Vector2D(2, 3)
        result1 = v * 2
        result2 = 2 * v
        self.assertEqual(result1, Vector2D(4, 6))
        self.assertEqual(result2, Vector2D(4, 6))
        self.assertIsNot(result1, v)

    def test_division(self):
        v = Vector2D(4, 6)
        result = v / 2
        self.assertEqual(result, Vector2D(2, 3))
        with self.assertRaises(TypeError):
            2 / v

    def test_addition(self):
        v1 = Vector2D(1, 2)
        v2 = Vector2D(3, 4)
        self.assertEqual(v1 + v2, Vector2D(4, 6))
        self.assertEqual(v1 + 2, Vector2D(3, 4))
        self.assertEqual(2 + v1, Vector2D(3, 4))

    def test_subtraction(self):
        v1 = Vector2D(5, 7)
        v2 = Vector2D(2, 3)
        self.assertEqual(v1 - v2, Vector2D(3, 4))
        self.assertEqual(v1 - 2, Vector2D(3, 5))

    def test_unary_minus(self):
        v = Vector2D(3, -4)
        self.assertEqual(-v, Vector2D(-3, 4))

    def test_conversion(self):
        v = Vector2D(3, 4)
        self.assertEqual(complex(v), complex(3, 4))
        self.assertTrue(isclose(float(v), 5.0))
        self.assertEqual(int(v), 5)

    def test_dot_product(self):
        v1 = Vector2D(1, 0)
        v2 = Vector2D(0, 1)
        self.assertEqual(v1 @ v2, 0)

    def test_get_angle(self):
        v1 = Vector2D(1, 0)
        v2 = Vector2D(0, 1)
        self.assertTrue(isclose(v1.get_angle(v2), pi / 2))
        with self.assertRaises(ValueError):
            v1.get_angle(Vector2D(0, 0))

    def test_conjugate(self):
        v = Vector2D(3, 4)
        self.assertEqual(v.conjugate(), Vector2D(3, -4))


if __name__ == "__main__":
    unittest.main()