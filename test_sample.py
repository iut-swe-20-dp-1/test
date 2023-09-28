import unittest
from main import add_value_to_stack

class TestStack(unittest.TestCase):
    def test_add_value_to_stack(self):
        print(self._testMethodName)
        actual = add_value_to_stack(["1", "2", "3"])
        expected = {"stack": ["1", "2", "3"]}
        self.assertEqual(actual, expected)

    def test_add_value_to_stack_fail(self):
        print(self._testMethodName)
        actual = add_value_to_stack(["1", "2", "3"])
        expected = {"stack": ["1", "3"]}
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()