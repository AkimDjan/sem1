import unittest
from uuid import UUID
from metrics import PeriodActiveUsers

class TestPeriodActiveUsers(unittest.TestCase):
    def test_initialization_with_invalid_values(self):
        # Тест на проверку неправильных значений при инициализации
        with self.assertRaises(TypeError):
            PeriodActiveUsers(accumulation_period="invalid")

        with self.assertRaises(ValueError):
            PeriodActiveUsers(accumulation_period=0)

        with self.assertRaises(ValueError):
            PeriodActiveUsers(accumulation_period=-1)

        with self.assertRaises(ValueError):
            PeriodActiveUsers(accumulation_period=0.4)  # Округляется до 0

    def test_initialization_with_valid_values(self):
        # Тест на корректную инициализацию
        pau = PeriodActiveUsers(accumulation_period=1)
        self.assertEqual(pau.accumulation_period, 1)
        self.assertEqual(pau.unique_users_amount, 0)

    def test_single_day_unique_users(self):
        # Тест с уникальными пользователями за 1 день
        pau = PeriodActiveUsers(accumulation_period=1)
        pau.add_active_users_for_curr_day([
            UUID("2509a9eb-2422-4b83-8911-f780eea815bb"),
            UUID("f52fc9b2-2ff2-4419-9f07-22267946b46e")
        ])
        self.assertEqual(pau.unique_users_amount, 2)

    def test_multiple_days_unique_users(self):
        # Тест с уникальными пользователями за несколько дней
        pau = PeriodActiveUsers(accumulation_period=3)
        pau.add_active_users_for_curr_day([
            UUID("52d6f353-4dd3-421b-b1c4-c35d2ae9ad66"),
            UUID("b6595baa-a23a-4e22-8656-079f84c7c3a4"),
        ])
        self.assertEqual(pau.unique_users_amount, 2)

        # День 2
        pau.add_active_users_for_curr_day([
            UUID("3f06aef7-bf3a-41f8-b571-3453a3b27aa9"),
            UUID("b6595baa-a23a-4e22-8656-079f84c7c3a4"),
        ])
        self.assertEqual(pau.unique_users_amount, 3)

        # День 3, тот же набор пользователей
        pau.add_active_users_for_curr_day([
            UUID("52d6f353-4dd3-421b-b1c4-c35d2ae9ad66"),
        ])
        self.assertEqual(pau.unique_users_amount, 3)

    def test_repeat_users_in_one_day(self):
        # Тест на проверку повторяющихся пользователей в одном дне
        pau = PeriodActiveUsers(accumulation_period=1)
        pau.add_active_users_for_curr_day([
            UUID("52d6f353-4dd3-421b-b1c4-c35d2ae9ad66"),
            UUID("52d6f353-4dd3-421b-b1c4-c35d2ae9ad66"),
            UUID("b6595baa-a23a-4e22-8656-079f84c7c3a4")
        ])
        self.assertEqual(pau.unique_users_amount, 2)

    def test_empty_user_list(self):
        # Тест с пустым набором пользователей за один день
        pau = PeriodActiveUsers(accumulation_period=3)
        pau.add_active_users_for_curr_day([])  # День без активных пользователей
        self.assertEqual(pau.unique_users_amount, 0)

    def test_remove_old_days_from_period(self):
        # Тест на проверку удаления старых дней из периода
        pau = PeriodActiveUsers(accumulation_period=2)

        # День 1
        pau.add_active_users_for_curr_day([
            UUID("52d6f353-4dd3-421b-b1c4-c35d2ae9ad66"),
            UUID("b6595baa-a23a-4e22-8656-079f84c7c3a4"),
        ])
        self.assertEqual(pau.unique_users_amount, 2)

        # День 2
        pau.add_active_users_for_curr_day([
            UUID("3f06aef7-bf3a-41f8-b571-3453a3b27aa9")
        ])
        self.assertEqual(pau.unique_users_amount, 3)

        # День 3 — первый день должен быть удален
        pau.add_active_users_for_curr_day([
            UUID("b6595baa-a23a-4e22-8656-079f84c7c3a4")
        ])
        self.assertEqual(pau.unique_users_amount, 2)  # "b6595baa" и "3f06aef7"


if __name__ == "__main__":
    unittest.main()


