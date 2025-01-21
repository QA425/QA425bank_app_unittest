import unittest

from develop import simple_funcs


class TestSimpleFuncs(unittest.TestCase):

    def test_01_func_for_test(self):
        self.assertEqual(simple_funcs.func_for_test(3, 5), 8)

    def test_02_fizz_buzz(self):
        self.assertEqual(simple_funcs.get_fizz_buzz(-1), "Ошибка: число не в диапазоне от 1 до 100")
        self.assertEqual(simple_funcs.get_fizz_buzz(101), "Ошибка: число не в диапазоне от 1 до 100")
        self.assertEqual(simple_funcs.get_fizz_buzz(15), "Fizz Buzz")
        self.assertEqual(simple_funcs.get_fizz_buzz(3), "Fizz")
        self.assertEqual(simple_funcs.get_fizz_buzz(5), "Buzz")
        self.assertEqual(simple_funcs.get_fizz_buzz(7), 7)

    def test_03_product_in_range(self):
        self.assertEqual(simple_funcs.product_in_range(5, 1), 120)
        self.assertEqual(simple_funcs.product_in_range(1, 5), 120)
