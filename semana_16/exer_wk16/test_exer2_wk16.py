import unittest
from exer2_wk16 import main as count_case_main

class TestExer2(unittest.TestCase):
    """Tests para la función que cuenta mayúsculas y minúsculas"""

    def test_case_1(self):
        result = count_case_main("I love Nation Sushi")
        self.assertEqual(result, (3, 13))

    def test_case_2(self):
        result = count_case_main("HELLO WORLD")
        self.assertEqual(result, (10, 0))

    def test_case_3(self):
        result = count_case_main("hola mundo")
        self.assertEqual(result, (0, 9))

if __name__ == "__main__":
    unittest.main()
