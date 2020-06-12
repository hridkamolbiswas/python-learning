import unittest
from calc import Calculator

class TestCalc(unittest.TestCase):

    def test_add(self):
        #result = Calculator().add(10,5)
        self.assertEqual(Calculator().add(10,5), 15)
        self.assertEqual(Calculator().add(100,-5), 95)

    def test_substract(self):
        #result = Calculator().add(10,5)
        self.assertEqual(Calculator().minus(10,5), 5)
        self.assertEqual(Calculator().minus(100,-5), 105)

    def test_multi(self):
        #result = Calculator().add(10,5)
        self.assertEqual(Calculator().multi(10,5), 50)
        self.assertEqual(Calculator().multi(100,-5), -500)

    def test_div(self):
        #result = Calculator().add(10,5)
        self.assertEqual(Calculator().div(10,5), 2)
        self.assertEqual(Calculator().div(100,2), 50)

    def test(self):
        pass

if __name__=='__main__':
    unittest.main()