import unittest
import operations

class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(operations.add(10, 5), 15)
        self.assertEqual(operations.add(10, -5), 5)
        self.assertEqual(operations.add(-1,-1), -2)

    def test_subtraction(self):
        self.assertEqual(operations.subtraction(10, 5), 5)
        self.assertEqual(operations.subtraction(5,-5), 10)

    def test_multiply(self):
        self.assertEqual(operations.multiply(2,2), 4)
        self.assertEqual(operations.multiply(2,-2), -4)
        self.assertEqual(operations.multiply(-2,-2), 4)

    def test_divide(self):
        self.assertEqual(operations.divide(4,2), 2)
        self.assertEqual(operations.divide(5,2), 2)
        self.assertRaises(ValueError, operations.divide, 10, 0)

if __name__ == "__main__":
    unittest.main()