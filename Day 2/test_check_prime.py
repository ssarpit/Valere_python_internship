import unittest
import check_prime as check


class TestCheckPrime(unittest.TestCase):
    def test_check(self):
        self.assertEqual(check.check_prime(2), True)
        self.assertEqual(check.check_prime(9), False)
        self.assertEqual(check.check_prime(6), False)
        self.assertRaises(ValueError, check.check_prime('name'))


if __name__ == '__main__':
    unittest.main()
