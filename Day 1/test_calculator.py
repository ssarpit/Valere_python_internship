import unittest
import calculator_using_function as calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, -2), -3)
        self.assertEqual(calc.add(-1, 2), 1)
        self.assertEqual(calc.add(5, -6), -1)

    def test_substract(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, -2), -3)
        self.assertEqual(calc.add(-1, 2), 1)
        self.assertEqual(calc.add(5, -6), -1)

    def test_multiply(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, -2), -3)
        self.assertEqual(calc.add(-1, 2), 1)
        self.assertEqual(calc.add(5, -6), -1)

    def test_divide(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, -2), -3)
        self.assertEqual(calc.add(-1, 2), 1)
        self.assertEqual(calc.add(5, -6), -1)
        self.assertRaises(ValueError, calc.divide, 10, 0)


if __name__ == '__main__':
    unittest.main()
