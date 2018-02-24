import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    def test_adds(self):
        result = rpn.calculate('1 1 + 2 +')
        self.assertEqual(4, result)
    def test_sub(self):
        result = rpn.calculate('5 2 -')
        self.assertEqual(3, result)
    def test_div(self):
        result = rpn.calculate('6 2 /')
        self.assertEqual(3, result)
    def test_mul(self):
        result = rpn.calculate('5 2 *')
        self.assertEqual(10, result)
    def test_percent(self):
        result = rpn.calculate('72 5 %')
        self.assertEqual(75.6, result)
    def test_pow(self):
        result = rpn.calculate('5 2 ^')
        self.assertEqual(25, result)
    def test_intdiv(self):
        result = rpn.calculate('5 2 .')
        self.assertEqual(2, result)
    def test_and(self):
        result = rpn.calculate('3 10 &')
        self.assertEqual(2, result)
    def test_or(self):
        result = rpn.calculate('2 7 |')
        self.assertEqual(7, result)
    def test_not(self):
        result = rpn.calculate('2 ~')
        self.assertEqual(False, result)
    def test_copy(self):
        result = rpn.calculate('copy')
        self.assertEqual(True, result)

