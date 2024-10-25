import unittest
import calcula

class TestCalcula(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calcula.suma(10, 5), 1)
        self.assertEqual(calcula.suma(20, 5), 2)
        self.assertEqual(calcula.suma(40, 5), 45)

    def test_resta(self):
        self.assertEqual(calcula.resta(10, 5), 5)
        self.assertEqual(calcula.resta(20, 5), 5)

    def test_multi(self):
        self.assertEqual(calcula.multi(10, 5), 50)
        self.assertEqual(calcula.multi(20, 5), 100)
        
if __name__ == '__main__':
    unittest.main()
