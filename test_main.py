from unittest import TestCase
import main


class TestMulti(TestCase):
    def test_multi(self):
        self.assertEqual(main.multi([3], [2]), [6])

    def test_multi_backwards(self):
        self.assertEqual(main.multi([2], [3]), [6])

    def test_multi_transfer(self):
        self.assertEqual(main.multi([4], [3]), [2, 1])

    def test_multi_transfer_backwards(self):
        self.assertEqual(main.multi([3], [4]), [2, 1])

    def test_multi_long(self):
        self.assertEqual(main.multi([9, 9], [7, 7]), [3, 2, 6, 7])

    def test_multi_long_long(self):
        self.assertEqual(main.multi([0, 0, 1], [0, 0, 2]), [0, 0, 0, 0, 2])

    def test_multi_zero(self):
        self.assertEqual(main.multi([0], [5]), [0])


class TestListToString(TestCase):
    def test_list_to_string_0(self):
        self.assertEqual(main.list_to_string([0]), "0")

    def test_list_to_string_5(self):
        self.assertEqual(main.list_to_string([5]), "5")

    def test_list_to_string_123(self):
        self.assertEqual(main.list_to_string([3, 2, 1]), "123")


class TestIntToList(TestCase):
    def test_int_to_list_0(self):
        self.assertEqual(main.int_to_list(0), [0])

    def test_int_to_list_5(self):
        self.assertEqual(main.int_to_list(5), [5])

    def test_int_to_list_123(self):
        self.assertEqual(main.int_to_list(123), [3, 2, 1])


class TestStringFactorial(TestCase):
    def test_factorial_1(self):
        self.assertEqual(main.string_factorial(1), "1")

    def test_factorial_0(self):
        self.assertEqual(main.string_factorial(0), "1")

    def test_factorial_5(self):
        self.assertEqual(main.string_factorial(5), "120")

    def test_factorial_10(self):
        self.assertEqual(main.string_factorial(10), "3628800")

    def test_factorial_20(self):
        self.assertEqual(main.string_factorial(20), "2432902008176640000")
