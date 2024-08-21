import unittest
from complejos1 import complex_sum, complex_subtract, complex_mult, complex_division, complex_corte2polar, complex_polar2carte, complex_phase, module,conjugate

class TestComplex(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(complex_sum([1, -2],[0, 0]), (1, -2))
        self.assertEqual(complex_sum([-8, 5],[3, 2]), (-5, 7))
    def test_subtract(self):
        self.assertEqual(complex_subtract([1, -2],[0, 0]), (1, -2))
        self.assertEqual(complex_subtract([-8, 5],[3, 2]), (-11, 3))
    def test_multiply(self):
        self.assertEqual(complex_mult([1, -2],[0, 0]), (0, 0))
        self.assertEqual(complex_mult([-8, 5],[3, 2]), (-34, -1))
    def test_division(self):
        self.assertEqual(complex_division([0, -3],[-1, -1]), (1.5, 1.5))
        self.assertEqual(complex_division([0, 0],[0, -1]), (0, 0))
    def test_carte2polar(self):
        self.assertEqual(complex_corte2polar([1, -1]),(1.4142135623730951, -0.7853981633974483))
        self.assertEqual(complex_corte2polar([-2, 1]),(2.23606797749979, -0.4636476090008061))
    def test_polar2corte(self):
        self.assertEqual(complex_polar2carte([2.24, -0.46]),(4.589293016703022, -1.0707092446824535))
        self.assertEqual(complex_polar2carte([2, 0]), (3.141592653589793, 0.0))
    def test_phase(self):
        self.assertEqual(complex_phase([5, 5]), 0.7853981633974483)
        self.assertEqual(complex_phase([1, 0]), 0.0)
    def test_module(self):
        self.assertEqual(module([4, -3]),5.0)
        self.assertEqual(module([4, 3]),5.0)
    def test_conjugate(self):
        self.assertEqual(conjugate([4, 3]), (4, -3))
        self.assertEqual(conjugate([4,-3]),(4, 3))
if __name__ == '__main__':
    unittest.main()
