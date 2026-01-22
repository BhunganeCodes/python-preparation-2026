import unittest
from main import (
    sum_numbers,
    reverse_list,
    remove_duplicates,
    fibonacci_series,
    char_frequency,
    factorial,
    is_palindrome
)


class TestMainFunctions(unittest.TestCase):

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(5), 15)
        self.assertEqual(sum_numbers(0), 0)
        self.assertEqual(sum_numbers(-5), 0)

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_list([]), [])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 1]), [1, 2, 3])
        self.assertEqual(remove_duplicates([]), [])

    def test_fibonacci_series(self):
        self.assertEqual(fibonacci_series(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_series(1), [0])
        self.assertEqual(fibonacci_series(0), [])


    def test_word_palindromes(self):  
        self.assertTrue(is_palindrome("Racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("a")) 
        self.assertTrue(is_palindrome(""))

        self.assertTrue(is_palindrome(12321))
        self.assertFalse(is_palindrome(123))
        self.assertTrue(is_palindrome("A man a plan a canal Panama".replace(" ", "").lower()))


    def test_char_frequency(self):
        self.assertEqual(char_frequency("aabb"), {'a': 2, 'b': 2})
        self.assertEqual(char_frequency(""), {})

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()
