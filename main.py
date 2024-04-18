import unittest
import sys

def addition(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_positive(self):
        result = addition(5, 6)
        self.assertEqual(result, 11)

    def test_negative(self):
        result = addition(-5, -6)
        self.assertEqual(result, -11)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py <test_function>")
        sys.exit(1)

    test_function = sys.argv[1]

    # Create a test suite with only the specified test function
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestAddition(test_function))

    # Run the test suite
    unittest.TextTestRunner().run(test_suite)
