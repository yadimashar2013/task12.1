import unittest
from student import Student


# Создайте в отдельном модуле класс для тестирования (наследованный от TestCase)
class StudentTest(unittest.TestCase):
    # Первый тест: у одного объекта должен запускать метод walk 10 раз,
    # после чего должен возвращаться результат сравнения полученных данных.
    # В  случае провального теста должно выводится сообщение:
    # Дистанции не равны [дистанция человека(объекта)] != 500
    def test_walk(self):
        self.student1 = Student('Идущего')
        for i in range(10):
            self.student1.walk()
        result1 = self.student1.distance
        self.assertEqual(result1, 500,
                        f'Дистанции не равны [дистанция человека {self.student1.name}] != 500')
    # Второй тест: у одного объекта должен запускать метод run 10 раз,
    # после чего должен возвращаться результат сравнения полученных данных.
    # В  случае провального теста должно выводится сообщение:
    #  Дистанции не равны [дистанция человека(объекта)] != 1000
    def test_run(self):
        self.student2 = Student('Бегущего')
        for k in range(10):
            self.student2.run()
        result2 = self.student2.distance
        self.assertEqual(result2, 1000,
                        f' Дистанции не равны [дистанция человека {self.student2.name}] != 1000')
    # Третий тест: 2 объекта "соревнуются", один "бежит", другой "идёт".
    # После чего должен возвращаться результат сравнения полученных данных.
    # В  случае провального теста должно выводится сообщение:
    # [бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек].
    def test_object_comparison(self):
        self.student1 = Student('Идущего')
        self.student2 = Student('Бегущего')
        self.student1.run(), self.student2.walk()
        result1 = self.student1.distance
        result2 = self.student2.distance
        self.assertGreater(result1, result2,
                        f'[бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек]')
        self.assertLess(result2, result1,
                        f'[бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек]')


if __name__ == '__main__':
    unittest.main()
