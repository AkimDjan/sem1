import pytest
from math import isclose

from VectorND import VectorND


# Тесты на инициализацию
def test_initialization():
    # Корректные случаи
    assert VectorND([1, 2, 3])  # Целые числа
    assert VectorND([1.0, 2.0, 3.0])  # Вещественные числа
    assert VectorND(range(10))  # Генератор
    assert VectorND((0, 1, 2))  # Кортеж

    # Некорректные случаи
    with pytest.raises(TypeError):
        VectorND("string")  # Не итерируемое
    with pytest.raises(TypeError):
        VectorND([1, "string", 2])  # Содержит не-число
    with pytest.raises(ValueError):
        VectorND([])  # Пустой список


# Тесты на строковое представление
def test_string_representation():
    assert str(VectorND([1, 2, 3])) == "VectorND(1, 2, 3)"
    assert str(VectorND(range(1000))) == "VectorND(0, 1, 2, 3...)"
    assert str(VectorND(range(1000))) == "VectorND(0, 1, 2, 3...)"
    assert str(VectorND([1.123456789, 2])) == "VectorND(1.12345678...)"  # Обрезка до 10 символов


# Тесты на итерируемость
def test_iteration():
    vector = VectorND([1, 2, 3])
    assert list(vector) == [1, 2, 3]


# Тесты на `len()`
def test_length():
    assert len(VectorND([1, 2, 3])) == 3
    assert len(VectorND(range(100))) == 100


# Тесты на оператор `in`
def test_in_operator():
    vector = VectorND([1, 2, 3])
    assert 1 in vector
    assert 3 in vector
    assert 4 not in vector
    with pytest.raises(TypeError):
        1.5 in vector  # Только целые числа


# Тесты на доступ по индексу
def test_indexing():
    vector = VectorND([1, 2, 3])
    assert vector[1] == 1
    assert vector[3] == 3
    with pytest.raises(IndexError):
        _ = vector[4]
    with pytest.raises(IndexError):
        _ = vector[0]


def test_equality():
    """Тесты на =="""
    assert VectorND([1, 2]) == VectorND([1, 2])  # равные вектора
    assert not VectorND([1, 2]) == VectorND([2, 1])  # разные компоненты
    assert VectorND([1, 2, 3]) == VectorND([1, 2, 3])  # одинаковые вектора
    assert not VectorND([3, 3]) == VectorND([4, 3])  # первый больше по первой компоненте
    assert not VectorND([1, 2]) == VectorND([1, 3])  # первый меньше по второй компоненте
    assert VectorND([1, 2]) == VectorND([1, 2])  # равные вектора
    assert VectorND([0, 0, 0]) == VectorND([0, 0, 0])  # равные вектора
    assert not VectorND([1, 1, 1]) == VectorND([1, 1, 2])  # разные по третьей компоненте
    assert VectorND([4, 5]) == VectorND([4, 5])  # равные вектора
    assert not VectorND([5, 6]) == VectorND([5, 5])  # первый больше по второй компоненте

    # 1. Первый и второй равны по всем компонентам
    assert VectorND([3, 4, 5]) == VectorND([3, 4, 5])  # одинаковые компоненты
    # 2. Разные длины (не равны)
    assert not VectorND([1, 2]) == VectorND([1, 2, 3])  # разные длины
    # 3. Равные по всем компонентам, но длина разная (недостающие компоненты считаются 0)
    assert VectorND([1, 2]) == VectorND([1, 2, 0])  # недостающий компонент равен 0
    # 4. Первый и второй равны по первой и второй компонентам
    assert VectorND([1, 2, 3]) == VectorND([1, 2, 3])  # одинаковые компоненты
    # 5. Равные вектора с одинаковыми компонентами
    assert VectorND([3, 3]) == VectorND([3, 3])

def test_not_equal():
    """Тесты на !="""
    assert not VectorND([1, 2]) != VectorND([1, 2])  # равные вектора
    assert VectorND([1, 2]) != VectorND([2, 1])  # разные компоненты
    assert not VectorND([1, 2, 3]) != VectorND([1, 2, 3])  # одинаковые вектора
    assert VectorND([3, 3]) != VectorND([4, 3])  # первый больше по первой компоненте
    assert VectorND([1, 2]) != VectorND([1, 3])  # первый меньше по второй компоненте
    assert not VectorND([1, 2]) != VectorND([1, 2])  # равные вектора
    assert not VectorND([0, 0, 0]) != VectorND([0, 0, 0])  # равные вектора
    assert VectorND([1, 1, 1]) != VectorND([1, 1, 2])  # разные по третьей компоненте
    assert not VectorND([4, 5]) != VectorND([4, 5])  # равные вектора
    assert VectorND([5, 6]) != VectorND([5, 5])  # первый больше по второй компоненте

    # 1. Разные по всем компонентам
    assert VectorND([3, 4, 5]) != VectorND([3, 4, 6])  # компоненты различаются
    # 2. Разные длины (не равны)
    assert VectorND([1, 2]) != VectorND([1, 2, 3])  # разные длины
    # 3. Равные по всем компонентам, но длина разная (недостающие компоненты считаются 0)
    assert not VectorND([1, 2]) != VectorND([1, 2, 0])  # недостающий компонент равен 0
    # 4. Первый и второй не равны по всем компонентам
    assert VectorND([1, 2, 3]) != VectorND([1, 3, 3])  # разные по второй компоненте
    # 5. Равные вектора с одинаковыми компонентами
    assert not VectorND([3, 3]) != VectorND([3, 3])  # одинаковые компоненты

def test_less():
    """ Тесты на < """
    assert VectorND([1, 2]) < VectorND([1, 3])
    assert VectorND([1, 2]) < VectorND([1, 2, 4, 1, 4, 1, 5, 7])
    assert not VectorND([1, 3]) < VectorND([1, 3])
    assert VectorND([3, 2]) < VectorND([3, 3])
    assert not VectorND([3]) < VectorND([3])

    # 1. Первый меньше по второй компоненте
    assert VectorND([3, 2]) < VectorND([3, 3])

    # 2. Первый меньше по первой компоненте
    assert VectorND([2, 5]) < VectorND([3, 5])

    # 3. Первый меньше по первой компоненте, вторая не сравнивается
    assert VectorND([1, 7]) < VectorND([2, 6])

    # 4. Первый меньше по третьей компоненте, первые две равны
    assert VectorND([4, 5, 6]) < VectorND([4, 5, 7])

    # 5. Первый короче, недостающие компоненты считаются 0
    assert VectorND([1, 2]) < VectorND([1, 2, 3])

    # 6. Первый больше по первой компоненте (не выполняется)
    assert not (VectorND([5, 3]) < VectorND([4, 4]))


    # 8. Первый меньше по второй компоненте, первая равна
    assert VectorND([4, 2]) < VectorND([4, 3])

    # 9. Первый полностью меньше
    assert VectorND([1, 1, 1]) < VectorND([2, 2, 2])

    # 10. Разные длины, второй больше за счет добавления значений
    assert VectorND([1, 2]) < VectorND([1, 2, 1])

    # 1. Первый вектор меньше по первой компоненте
    v1 = VectorND([0, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert v1 < v2  # True

    # 2. Первый вектор равен второму (не меньше)
    v1 = VectorND([1, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert not (v1 < v2)  # False

    # 3. Первый вектор больше по первой компоненте
    v1 = VectorND([2, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert not (v1 < v2)  # False

    # 4. Разные размерности, первый меньше с учетом недостающих нулей
    v1 = VectorND([1, 2])
    v2 = VectorND([1, 2, 3])
    assert v1 < v2  # True

    # 5. Разные размерности, первый не меньше с учетом недостающих нулей
    v1 = VectorND([1, 2, 4])
    v2 = VectorND([1, 2])
    assert not (v1 < v2)  # False

    # 6. Первый вектор меньше только по одной компоненте
    v1 = VectorND([1, 2, 2])
    v2 = VectorND([1, 2, 3])
    assert v1 < v2  # True

    # 7. Первый вектор больше только по последней компоненте
    v1 = VectorND([1, 2, 4])
    v2 = VectorND([1, 2, 3])
    assert not (v1 < v2)  # False

    # 8. Все компоненты первого вектора меньше
    v1 = VectorND([0, 0, 0])
    v2 = VectorND([1, 2, 3])
    assert v1 < v2  # True

    # 9. Первый вектор равен нулевому вектору, второй ненулевой
    v1 = VectorND([0, 0, 0])
    v2 = VectorND([1, 1, 1])
    assert v1 < v2  # True

    # 10. Первый вектор имеет одинаковые компоненты, кроме последнего
    v1 = VectorND([1, 2, 2])
    v2 = VectorND([1, 2, 3])
    assert v1 < v2  # True


def test_more():
    """Тесты на > """
    assert VectorND([1, 3]) > VectorND([1, 2])
    assert VectorND([1, 4]) > VectorND([1, 2])
    assert not VectorND([1, 1]) > VectorND([1, 2])
    assert not VectorND([0, 3]) > VectorND([1, 2])

    # 1. Первый больше по второй компоненте
    assert VectorND([3, 4]) > VectorND([3, 3])

    # 2. Первый больше по первой компоненте
    assert VectorND([4, 5]) > VectorND([3, 5])

    # 3. Первый больше по первой компоненте, вторая не сравнивается
    assert VectorND([3, 7]) > VectorND([2, 8])

    # 4. Первый больше по третьей компоненте, первые две равны
    assert VectorND([4, 5, 8]) > VectorND([4, 5, 7])

    # 5. Второй короче, недостающие компоненты считаются 0
    assert VectorND([1, 2, 3]) > VectorND([1, 2])

    # 6. Первый меньше по первой компоненте (не выполняется)
    assert not (VectorND([2, 3]) > VectorND([3, 4]))

    # 8. Первый больше по второй компоненте, первая равна
    assert VectorND([4, 5]) > VectorND([4, 4])

    # 9. Первый полностью больше
    assert VectorND([3, 3, 3]) > VectorND([2, 2, 2])

    # 10. Разные длины, первый больше за счет добавления значений
    assert VectorND([1, 2, 1]) > VectorND([1, 2])


def test_less_or_eq():
    """Тесты на <= """
    assert VectorND([1, 2]) <= VectorND([1, 3])  # первый меньше по второй компоненте
    assert VectorND([1, 2]) <= VectorND([1, 2])  # равные вектора
    assert not VectorND([3, 4]) <= VectorND([3, 3])  # первый больше по второй компоненте
    assert VectorND([1, 2]) <= VectorND([3, 4])  # первый меньше по обеим компонентам
    assert not VectorND([2, 3]) <= VectorND([1, 2])  # первый больше по первой компоненте
    assert VectorND([3, 3]) <= VectorND([4, 3])  # первый меньше по первой компоненте
    assert VectorND([4, 5]) <= VectorND([4, 5])  # равные вектора
    assert VectorND([1, 2, 3]) <= VectorND([1, 2, 4])  # первый меньше по третьей компоненте
    assert not VectorND([2, 3]) <= VectorND([2, 2])  # первый больше по второй компоненте
    assert VectorND([3, 3]) <= VectorND([3, 4])  # равные по первой компоненте, второй меньше
    assert VectorND([1, 1, 1]) <= VectorND([1, 1, 2])  # равные по первым двум, третий меньше
    assert VectorND([0, 0, 0]) <= VectorND([1, 1, 1])  # первый полностью меньше
    assert not VectorND([5, 5]) <= VectorND([4, 4])  # первый больше по обеим компонентам
    assert VectorND([2, 3]) <= VectorND([2, 3])  # равные вектора
    assert VectorND([1, 2]) <= VectorND([2, 3])  # первый меньше по обеим компонентам
    assert VectorND([2, 4]) <= VectorND([3, 4])  # первый меньше по первой компоненте
    assert VectorND([1, 2, 3]) <= VectorND([1, 2, 3])  # одинаковые вектора
    assert VectorND([3, 3, 3]) <= VectorND([4, 4, 4])  # все компоненты меньше
    assert VectorND([2, 1, 3]) <= VectorND([3, 2, 3])  # первый меньше по первой и второй компонентам
    assert VectorND([1, 2, 1]) <= VectorND([1, 2, 1])  # равные вектора

    assert VectorND([1, 2]) <= VectorND([1, 2])

    # 1. Равные векторы
    v1 = VectorND([1, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert v1 <= v2  # True

    # 2. Первый вектор меньше по первой компоненте
    v1 = VectorND([0, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert v1 <= v2  # True

    # 3. Первый вектор больше по первой компоненте
    v1 = VectorND([2, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert not (v1 <= v2)  # False

    # 4. Разные размерности, вектор меньшей размерности заполняется нулями
    v1 = VectorND([1, 2])
    v2 = VectorND([1, 2, 3])
    assert v1 <= v2  # True

    # 5. Разные размерности, первый вектор больше с учетом недостающих компонентов
    v1 = VectorND([1, 2, 4])
    v2 = VectorND([1, 2])
    assert not (v1 <= v2)  # False

    # 6. Первый вектор равен вектору с нулями в недостающих компонентах
    v1 = VectorND([1, 2])
    v2 = VectorND([1, 2, 0])
    assert v1 <= v2  # True

    # 7. Все элементы первого вектора меньше
    v1 = VectorND([0, 0, 0])
    v2 = VectorND([1, 2, 3])
    assert v1 <= v2  # True

    # 8. Первый вектор имеет одинаковые компоненты, кроме одного меньшего
    v1 = VectorND([1, 2, 2])
    v2 = VectorND([1, 2, 3])
    assert v1 <= v2  # True

    # 9. Первый вектор больше по последнему элементу
    v1 = VectorND([1, 2, 4])
    v2 = VectorND([1, 2, 3])
    assert not (v1 <= v2)  # False

    # 10. Первый вектор равен нулевому вектору
    v1 = VectorND([0, 0, 0])
    v2 = VectorND([0, 0])
    assert v1 <= v2  # True

    # 11 Разные размерности, вектор меньшей размерности имеет нули
    v1 = VectorND([1, 2])
    v2 = VectorND([1, 2, 0])
    assert v1 <= v2  # True

    # 12 Разные размерности, вектор меньшей размерности имеет нули
    v2 = VectorND([1, 2, 0])
    v1 = VectorND([1, 2])
    assert v2 <= v1  # True


def test_more_or_eq():
    """Тесты на >="""
    assert VectorND([1, 3]) >= VectorND([1, 2])  # первый больше по второй компоненте
    assert VectorND([1, 2]) >= VectorND([1, 2])  # равные вектора
    assert not VectorND([1, 1]) >= VectorND([1, 2])  # первый меньше по второй компоненте
    assert not VectorND([0, 3]) >= VectorND([1, 2])  # первый меньше по первой компоненте

    # 1. Первый больше по второй компоненте
    assert VectorND([3, 4]) >= VectorND([3, 3])

    # 2. Первый больше по первой компоненте
    assert VectorND([4, 5]) >= VectorND([3, 5])

    # 3. Первый больше по первой компоненте, вторая не сравнивается
    assert VectorND([3, 7]) >= VectorND([2, 8])

    # 4. Первый больше по третьей компоненте, первые две равны
    assert VectorND([4, 5, 8]) >= VectorND([4, 5, 7])

    # 5. Второй короче, недостающие компоненты считаются 0
    assert VectorND([1, 2, 3]) >= VectorND([1, 2])

    # 6. Первый меньше по первой компоненте (не выполняется)
    assert not (VectorND([2, 3]) >= VectorND([3, 4]))

    # 7. Первый больше по первой компоненте и второй равны
    assert VectorND([4, 5]) >= VectorND([4, 4])

    # 8. Первый полностью больше
    assert VectorND([3, 3, 3]) >= VectorND([2, 2, 2])

    # 9. Разные длины, первый больше за счет добавления значений
    assert VectorND([1, 2, 1]) >= VectorND([1, 2])

    # 10. Первый больше по второй компоненте
    assert VectorND([1, 5]) >= VectorND([1, 4])

    # 11. Первый больше по обеим компонентам
    assert VectorND([4, 5]) >= VectorND([3, 4])

    # 12. Первый меньше по второй компоненте
    assert not VectorND([3, 2]) >= VectorND([3, 3])

    # 13. Первый больше по первой компоненте
    assert VectorND([2, 3]) >= VectorND([1, 3])

    # 14. Первый больше по первой и второй компонентам
    assert VectorND([4, 4]) >= VectorND([3, 3])

    # 15. Первый больше по первой компоненте, второй равны
    assert VectorND([2, 3]) >= VectorND([1, 3])

    # 16. Первый равен второму
    assert VectorND([2, 2]) >= VectorND([2, 2])

    # 17. Первый меньше по обеим компонентам (не выполняется)
    assert not VectorND([1, 1]) >= VectorND([2, 2])

    # 18. Первый больше по первой компоненте и равен по второй
    assert VectorND([3, 3]) >= VectorND([2, 3])

    # 19. Первый больше по первой и третьей компонентам
    assert VectorND([4, 5, 6]) >= VectorND([3, 5, 4])

    # 20. Векторы одинаковой длины, но разные компоненты
    assert VectorND([5, 5]) >= VectorND([4, 5])

    assert VectorND([1, 3]) >= VectorND([1, 2])
    # 1. Равные векторы
    v1 = VectorND([1, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert v1 >= v2  # True

    # 2. Первый вектор больше по первой компоненте
    v1 = VectorND([2, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert v1 >= v2  # True

    # 3. Первый вектор меньше по первой компоненте
    v1 = VectorND([0, 2, 3])
    v2 = VectorND([1, 2, 3])
    assert not (v1 >= v2)  # False

    # 4. Разные размерности, вектор меньшей размерности имеет нули
    v1 = VectorND([1, 2])
    v2 = VectorND([1, 2, 0])
    assert v1 >= v2  # True

    # 5. Разные размерности, вектор меньшей размерности меньше
    v1 = VectorND([1, 2])
    v2 = VectorND([1, 2, 1])
    assert not (v1 >= v2)  # False

    # 6. Разные размерности, большее значение в меньшем векторе
    v1 = VectorND([1, 3])
    v2 = VectorND([1, 2, 0])
    assert v1 >= v2  # True

    # 7. Первый вектор больше по последнему элементу
    v1 = VectorND([1, 2, 4])
    v2 = VectorND([1, 2, 3])
    assert v1 >= v2  # True

    # 8. Все элементы первого вектора меньше
    v1 = VectorND([0, 0, 0])
    v2 = VectorND([1, 2, 3])
    assert not (v1 >= v2)  # False

    # 9. Первый вектор имеет одинаковые компоненты, кроме одного большего
    v1 = VectorND([1, 2, 4])
    v2 = VectorND([1, 2, 3])
    assert v1 >= v2  # True

    # 10. Первый вектор равен нулевому вектору
    v1 = VectorND([0, 0, 0])
    v2 = VectorND([0, 0, 0])
    assert v1 >= v2  # True


# Тесты на длину вектора (abs)
def test_abs():
    assert abs(VectorND([3, 4])) == 5
    assert isclose(abs(VectorND([1, 2, 2])), 3)


# Тесты на преобразование в bool
def test_bool_conversion():
    assert bool(VectorND([1, 0, 0])) is True
    assert bool(VectorND([0, 0, 0])) is False


# Тесты на умножение на число
def test_multiplication():
    vector = VectorND([1, 2, 3])
    result = vector * 2
    assert result == VectorND([2, 4, 6])
    result = 2 * vector
    assert result == VectorND([2, 4, 6])


# Тесты на деление на число
def test_division():
    """Тесты на деление на число"""

    assert VectorND([2, 4]) / 2 == VectorND([1, 2])  # 2/2, 4/2 = [1, 2]
    assert VectorND([2, 4]) / -2 == VectorND([-1, -2])  # 2/-2, 4/-2 = [-1, -2]
    assert VectorND([3, 6]) / 1 == VectorND([3, 6])  # 3/1, 6/1 = [3, 6]
    # Деление на число 0 (выбрасывается ошибка)
    try:
        VectorND([2, 4]) / 0
        assert False, "Expected division by zero error"
    except ValueError:
        pass  # Ожидаем ошибку деления на ноль
    assert VectorND([0, 0]) / 2 == VectorND([0, 0])  # 0/2, 0/2 = [0, 0]
    assert VectorND([2, 4]) / 0.5 == VectorND([4, 8])  # 2/0.5, 4/0.5 = [4, 8]
    assert VectorND([2, 4]) / -0.5 == VectorND([-4, -8])  # 2/-0.5, 4/-0.5 = [-4, -8]
    assert VectorND([1, 2]) / 1000000 == VectorND([1e-06, 2e-06])  # 1/1000000, 2/1000000 = [1e-06, 2e-06]
    assert VectorND([1, 2]) / 1e-6 == VectorND([1e6, 2e6])  # 1/1e-6, 2/1e-6 = [1e6, 2e6]
    assert VectorND([1, 2]) / -1000000 == VectorND([-1e-06, -2e-06])  # 1/-1000000, 2/-1000000 = [-1e-06, -2e-06]
    assert VectorND([2, 4]) / 2.5 == VectorND([0.8, 1.6])  # 2/2.5, 4/2.5 = [0.8, 1.6]
    assert VectorND([-2, -4]) / 2 == VectorND([-1, -2])  # -2/2, -4/2 = [-1, -2]
    assert VectorND([2, 4]) / 0.2 == VectorND([10, 20])  # 2/0.2, 4/0.2 = [10, 20]
    assert VectorND([2, 4]) / -0.2 == VectorND([-10, -20])  # 2/-0.2, 4/-0.2 = [-10, -20]
    assert VectorND([4]) / 2 == VectorND([2])  # 4/2 = [2]
    assert VectorND([1000]) / 1000 == VectorND([1])  # 1000/1000 = [1]
    assert VectorND([2.5, 5.5]) / 2 == VectorND([1.25, 2.75])  # 2.5/2, 5.5/2 = [1.25, 2.75]
    assert VectorND([0.5, 1.5]) / 0.5 == VectorND([1, 3])  # 0.5/0.5, 1.5/0.5 = [1, 3]
    assert VectorND([0.5, 1.5]) / -0.5 == VectorND([-1, -3])  # 0.5/-0.5, 1.5/-0.5 = [-1, -3]
    assert VectorND([1000, 2000]) / 2 == VectorND([500, 1000])  # 1000/2, 2000/2 = [500, 1000]
    assert VectorND([0, 1000]) / 2 == VectorND([0, 500])  # 0/2, 1000/2 = [0, 500]
    assert VectorND([1000000, 2000000]) / 1000000 == VectorND([1, 2])  # 1000000/1000000, 2000000/1000000 = [1, 2]
    assert VectorND([1000, 2000]) / -2 == VectorND([-500, -1000])  # 1000/-2, 2000/-2 = [-500, -1000]
    assert VectorND([-2, -4]) / 0.5 == VectorND([-4, -8])  # -2/0.5, -4/0.5 = [-4, -8]
    assert VectorND([2, 4]) / -0.5 == VectorND([-4, -8])  # 2/-0.5, 4/-0.5 = [-4, -8]
    assert VectorND([0, 0]) / 0.5 == VectorND([0, 0])  # 0/0.5, 0/0.5 = [0, 0]
    assert VectorND([0, 0]) / -2 == VectorND([0, 0])  # 0/-2, 0/-2 = [0, 0]
    assert VectorND([1, 2]) / 1e-6 == VectorND([1e6, 2e6])  # 1/1e-6, 2/1e-6 = [1e6, 2e6]
    assert VectorND([1, 2]) / 1000000 == VectorND([1e-06, 2e-06])  # 1/1000000, 2/1000000 = [1e-06, 2e-06]

def test_add_with_number():
    """Тесты на сложение с числом (слева и справа)"""

    assert VectorND([1, 2]) + 3 == VectorND([4, 5])  # 1+3, 2+3 = [4, 5]
    assert 3 + VectorND([1, 2]) == VectorND([4, 5])  # 3+1, 3+2 = [4, 5]
    assert VectorND([0, 0]) + 5 == VectorND([5, 5])  # 0+5, 0+5 = [5, 5]
    assert VectorND([3, 3]) + 2 == VectorND([5, 5])  # 3+2, 3+2 = [5, 5]
    assert VectorND([5, 5]) + -2 == VectorND([3, 3])  # 5-2, 5-2 = [3, 3]
    assert VectorND([1, 1]) + 0 == VectorND([1, 1])  # 1+0, 1+0 = [1, 1]
    assert VectorND([-1, -2]) + 3 == VectorND([2, 1])  # -1+3, -2+3 = [2, 1]
    assert VectorND([3, 2]) + -1 == VectorND([2, 1])  # 3-1, 2-1 = [2, 1]
    assert VectorND([100, 200]) + 50 == VectorND([150, 250])  # 100+50, 200+50 = [150, 250]
    assert VectorND([0, 100]) + 50 == VectorND([50, 150])  # 0+50, 100+50 = [50, 150]
    assert VectorND([1.5, 2.5]) + 0.5 == VectorND([2.0, 3.0])  # 1.5+0.5, 2.5+0.5 = [2.0, 3.0]
    assert VectorND([10.5, 20.5]) + 0.5 == VectorND([11.0, 21.0])  # 10.5+0.5, 20.5+0.5 = [11.0, 21.0]
    assert VectorND([1.5, 2.5]) + -0.5 == VectorND([1.0, 2.0])  # 1.5-0.5, 2.5-0.5 = [1.0, 2.0]
    assert VectorND([0, 0]) + 1 == VectorND([1, 1])  # 0+1, 0+1 = [1, 1]

def test_add_with_VectorND():
    """Тесты на сложение с другим объектом VectorND"""
    assert VectorND([1, 2]) + VectorND([1, 2]) == VectorND([2, 4])  # 1+1, 2+2 = [2, 4]
    assert VectorND([1, 2]) + VectorND([1, 2, 3]) == VectorND([2, 4, 3])  # 1+1, 2+2, 0+3 = [2, 4, 3]
    assert VectorND([0, 0]) + VectorND([2, 3]) == VectorND([2, 3])  # 0+2, 0+3 = [2, 3]
    assert VectorND([-1, -2]) + VectorND([2, 3]) == VectorND([1, 1])  # -1+2, -2+3 = [1, 1]
    assert VectorND([1, 1]) + VectorND([1, 1, 1]) == VectorND([2, 2, 1])  # 1+1, 1+1, 0+1 = [2, 2, 1]
    assert VectorND([100, 200]) + VectorND([50, 50]) == VectorND([150, 250])  # 100+50, 200+50 = [150, 250]
    assert VectorND([1.5, 2.5]) + VectorND([0.5, 1.5]) == VectorND([2.0, 4.0])  # 1.5+0.5, 2.5+1.5 = [2.0, 4.0]
    assert VectorND([0, 0, 0]) + VectorND([1, 1, 1]) == VectorND([1, 1, 1])  # 0+1, 0+1, 0+1 = [1, 1, 1]
    assert VectorND([1, 2, 3]) + VectorND([4, 5, 6]) == VectorND([5, 7, 9])  # 1+4, 2+5, 3+6 = [5, 7, 9]
    assert VectorND([1, 2]) + VectorND([1, 2, 3]) == VectorND([2, 4, 3])  # 1+1, 2+2, 0+3 = [2, 4, 3]
    assert VectorND([10, 20, 30, 40]) + VectorND([1, 2, 3, 4]) == VectorND(
        [11, 22, 33, 44])  # 10+1, 20+2, 30+3, 40+4 = [11, 22, 33, 44]
    assert VectorND([1.5, 2.5]) + VectorND([2, 3]) == VectorND([3.5, 5.5])  # 1.5+2, 2.5+3 = [3.5, 5.5]
    assert VectorND([-1, -2, -3]) + VectorND([1, 2, 3]) == VectorND([0, 0, 0])  # -1+1, -2+2, -3+3 = [0, 0, 0]

def test_subtraction():
    vector = VectorND([3, 2, 1])
    result = vector - 1
    assert result == VectorND([2, 1, 0])
    result = 1 - vector
    assert result == VectorND([-2, -1, 0])
    result = vector - VectorND([1, 1, 1])
    assert result == VectorND([2, 1, 0])


# Тесты на унарный минус
def test_unary_minus():
    vector = VectorND([1, -2, 3])
    assert -vector == VectorND([-1, 2, -3])


# Тесты на преобразование в `int` и `float`
def test_conversion():
    vector = VectorND([3, 4])
    assert int(vector) == 5
    assert float(vector) == 5.0


# Тесты на скалярное произведение (@)
def test_dot_product():
    """Тесты на оператор @ (скалярное произведение)"""
    assert VectorND([1, 2]) @ VectorND([2, 3]) == 8  # 1*2 + 2*3 = 8
    assert VectorND([1, 2, 3]) @ VectorND([3, 2, 1]) == 10  # 1*3 + 2*2 + 3*1 = 10
    assert VectorND([0, 1]) @ VectorND([1, 0, 1]) == 0  # 0*1 + 1*0 = 0
    assert VectorND([1, 1, 1]) @ VectorND([1, 1, 1]) == 3  # 1*1 + 1*1 + 1*1 = 3
    assert VectorND([1, 1]) @ VectorND([2, 2]) == 4  # 1*2 + 1*2 = 4
    assert VectorND([1, 2, 3]) @ VectorND([0, 0, 0]) == 0  # 1*0 + 2*0 + 3*0 = 0
    assert VectorND([2, 3]) @ VectorND([4, 5]) == 23  # 2*4 + 3*5 = 23
    assert VectorND([1, 1, 1]) @ VectorND([1, 0, 0]) == 1  # 1*1 + 1*0 + 1*0 = 1
    assert VectorND([0, 0]) @ VectorND([0, 0, 0]) == 0  # 0*0 + 0*0 = 0
    assert VectorND([1, 2, 3]) @ VectorND([1, 0]) == 1  # 1*1 + 2*0 + 3*0 = 1
    assert VectorND([1, 2, 3, 4]) @ VectorND([4, 3, 2, 1]) == 20  # 1*4 + 2*3 + 3*2 + 4*1 = 20
    assert VectorND([1, 1]) @ VectorND([1, 2]) == 3  # 1*1 + 1*2 = 3
    assert VectorND([0, 0, 0]) @ VectorND([1, 2, 3]) == 0  # 0*1 + 0*2 + 0*3 = 0
    assert VectorND([2, 4]) @ VectorND([4, 2]) == 16  # 2*4 + 4*2 = 16
    assert VectorND([3, 3]) @ VectorND([1, 1]) == 6  # 3*1 + 3*1 = 6
    assert VectorND([1, 2, 3]) @ VectorND([4, 5, 6]) == 32  # 1*4 + 2*5 + 3*6 = 32
    assert VectorND([1, 0]) @ VectorND([0, 1]) == 0  # 1*0 + 0*1 = 0
    assert VectorND([2, 2]) @ VectorND([2, 2]) == 8  # 2*2 + 2*2 = 8
    assert VectorND([1, 1, 0]) @ VectorND([1, 1, 1]) == 2  # 1*1 + 1*1 + 0*1 = 2
    assert VectorND([1, 1, 1]) @ VectorND([1, 0, 1]) == 2  # 1*1 + 1*0 + 1*1 = 2
    assert VectorND([1, 2, 3, 4]) @ VectorND([1, 1, 1, 1]) == 10  # 1*1 + 2*1 + 3*1 + 4*1 = 10
    assert VectorND([1, 1]) @ VectorND([2, 3]) == 5  # 1*2 + 1*3 = 5
    assert VectorND([1, 2]) @ VectorND([1, 1]) == 3  # 1*1 + 2*1 = 3
    assert VectorND([1, 2, 3]) @ VectorND([0, 0, 1]) == 3  # 1*0 + 2*0 + 3*1 = 3
    assert VectorND([2, 3]) @ VectorND([5, 5]) == 25  # 2*5 + 3*5 = 25
    assert VectorND([3, 3]) @ VectorND([4, 4]) == 24  # 3*4 + 3*4 = 24
    assert VectorND([1, 1, 1]) @ VectorND([1, 1, 0]) == 2  # 1*1 + 1*1 + 1*0 = 2
    assert VectorND([5, 0]) @ VectorND([0, 5]) == 0  # 5*0 + 0*5 = 0
    assert VectorND([1, 2]) @ VectorND([1, 1]) == 3  # 1*1 + 2*1 = 3
    assert VectorND([2, 3]) @ VectorND([2, 1]) == 7  # 2*2 + 3*1 = 7
    assert VectorND([1, 0]) @ VectorND([1, 1]) == 1  # 1*1 + 0*1 = 1
    assert VectorND([1, 1, 0]) @ VectorND([1, 0, 1]) == 1  # 1*1 + 1*0 + 0*1 = 1
    assert VectorND([1, 2, 3]) @ VectorND([1, 2, 3]) == 14  # 1*1 + 2*2 + 3*3 = 14
    assert VectorND([1, 1, 1, 1]) @ VectorND([1, 1, 1, 1]) == 4  # 1*1 + 1*1 + 1*1 + 1*1 = 4
    assert VectorND([0, 0]) @ VectorND([1, 2, 3]) == 0  # 0*1 + 0*2 + 0*3 = 0
