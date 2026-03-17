import unittest
from exer1_wk16 import main as sort_words_main

class TestExer1(unittest.TestCase):
    """Tests para la función que ordena palabras separadas por guion"""

    def test_case_1(self):
        text = "python-variable-computadora-monitor"
        result = sort_words_main(text)
        self.assertEqual(result, "computadora-monitor-python-variable")

    def test_case_2(self):
        text = "b-a-d-c"
        result = sort_words_main(text)
        self.assertEqual(result, "a-b-c-d")

    def test_case_3(self):
        text = "carro-casa-cielo-cama"
        result = sort_words_main(text)
        self.assertEqual(result, "carro-casa-cielo-cama")

if __name__ == "__main__":
    unittest.main()
