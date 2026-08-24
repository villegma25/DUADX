import unittest
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_small_list(self):
        """1️⃣ Funciona con una lista pequeña."""
        data = [5, 3, 1, 4, 2]
        result = bubble_sort(data)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_large_list(self):
        """2️⃣ Funciona con una lista grande (más de 100 elementos)."""
        data = list(range(200, 0, -1))  # 200 elementos en orden descendente
        result = bubble_sort(data)
        self.assertEqual(result, list(range(1, 201)))

    def test_empty_list(self):
        """3️⃣ Funciona con una lista vacía."""
        data = []
        result = bubble_sort(data)
        self.assertEqual(result, [])

    def test_invalid_parameter(self):
        """4️⃣ No funciona con parámetros que no sean lista."""
        with self.assertRaises(TypeError):
            bubble_sort("no es una lista")
        with self.assertRaises(TypeError):
            bubble_sort(123)
        with self.assertRaises(TypeError):
            bubble_sort({1, 2, 3})

if __name__ == '__main__':
    unittest.main()
