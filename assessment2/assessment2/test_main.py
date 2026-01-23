import unittest
from main import (
    is_anagram,
    find_anagram_groups,
    dict_keys_to_sorted_list,
    merge_dictionaries,
    count_vowels,
    remove_vowels,
    is_prime,
    custom_sort)

class TestPythonAssessment(unittest.TestCase):

    # ---------- is_anagram ----------
    def test_is_anagram_true(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("Dormitory", "dirty room"))
        self.assertTrue(is_anagram("The eyes", "They see"))

    def test_is_anagram_false(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("python", "java"))

    def test_is_anagram_edge_cases(self):
        self.assertTrue(is_anagram("", ""))
        self.assertFalse(is_anagram("a", "b"))

    # ---------- find_anagram_groups ----------
    def test_find_anagram_groups_basic(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        result = find_anagram_groups(words)
        # Convert to sets for order-insensitive comparison
        self.assertEqual([set(g) for g in result], [set(g) for g in expected])

    def test_find_anagram_groups_single(self):
        self.assertEqual(find_anagram_groups(["hello"]), [["hello"]])

    def test_find_anagram_groups_empty(self):
        self.assertEqual(find_anagram_groups([]), [])

    # ---------- dict_keys_to_sorted_list ----------
    def test_dict_keys_to_sorted_list(self):
        d = {"z": 1, "a": 2, "b": 3}
        self.assertEqual(dict_keys_to_sorted_list(d), ["a", "b", "z"])

    def test_dict_keys_to_sorted_list_empty(self):
        self.assertEqual(dict_keys_to_sorted_list({}), [])

    # ---------- merge_dictionaries ----------
    def test_merge_dictionaries_overlap(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        expected = {"a": 1, "b": 5, "c": 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_merge_dictionaries_no_overlap(self):
        dict1 = {"x": 10}
        dict2 = {"y": 20}
        self.assertEqual(merge_dictionaries(dict1, dict2), {"x": 10, "y": 20})

    def test_merge_dictionaries_empty(self):
        self.assertEqual(merge_dictionaries({}, {}), {})

    # ---------- count_vowels ----------
    def test_count_vowels_basic(self):
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("AEIOUaeiou"), 10)

    def test_count_vowels_no_vowels(self):
        self.assertEqual(count_vowels("rhythm"), 0)

    
    def test_remove_vowels_basic(self):
        self.assertEqual(remove_vowels("programming"), "prgrmmng")
        self.assertEqual(remove_vowels("AEIOUaeiou"), "")

    def test_remove_vowels_no_vowels(self):
        self.assertEqual(remove_vowels("xyz"), "xyz")

    # ---------- is_prime ----------
    def test_is_prime_true(self):
        for n in [2, 3, 5, 7, 11, 13, 17]:
            self.assertTrue(is_prime(n))

    def test_is_prime_false(self):
        for n in [0, 1, 4, 6, 8, 9, 10, 12]:
            self.assertFalse(is_prime(n))

    # ---------- custom_sort ----------
    def test_custom_sort_basic(self):
        words = ["banana", "apple", "cherry", "date"]
        expected = ["date", "apple", "banana", "cherry"]
        self.assertEqual(custom_sort(words), expected)

    def test_custom_sort_same_length(self):
        words = ["dog", "bat", "ant"]
        expected = ["ant", "bat", "dog"]
        self.assertEqual(custom_sort(words), expected)

    def test_custom_sort_empty(self):
        self.assertEqual(custom_sort([]), [])


if __name__ == "__main__":
    unittest.main()
