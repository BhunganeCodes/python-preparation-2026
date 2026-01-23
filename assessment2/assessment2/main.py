"""
Python Programming Assessment
Complete all functions below. Each function has a docstring with examples.
"""
from typing import List, Dict, Set, Tuple

def is_anagram(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams (ignoring case and spaces).
    
    Example:
        Input → str1 = "listen", str2 = "silent"
        Output → True
        
        Input → str1 = "hello", str2 = "world"
        Output → False
    """
    string1 = [char.lower() for char in str1 if char.isalpha()]
    string2 = [char.lower() for char in str2 if char.isalpha()]
    return sorted(string1) == sorted(string2)


def find_anagram_groups(words: List[str]) -> List[List[str]]:
    """
    Group words that are anagrams of each other.
    
    Example:
        Input → words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        Output → [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    """
    pass



def dict_keys_to_sorted_list(d: Dict) -> List[str]:
    """
    Convert dictionary keys to a sorted list.
    
    Example:
        Input → d = {"z": 1, "a": 2, "b": 3}
        Output → ["a", "b", "z"]
    """
    pass


def merge_dictionaries(dict1: Dict, dict2: Dict) -> Dict:
    """
    Merge two dictionaries. If keys overlap, sum their values.
    
    Example:
        Input → dict1 = {"a": 1, "b": 2}, dict2 = {"b": 3, "c": 4}
        Output → {"a": 1, "b": 5, "c": 4}
    """
    pass





def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string (case-insensitive).
    
    Example:
        Input → s = "Hello World"
        Output → 3
    """
    pass


def remove_vowels(s: str) -> str:
    """
    Remove all vowels from a string.
    
    Example:
        Input → s = "programming"
        Output → "prgrmmng"
    """
    pass



def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    Example:
        Input → n = 7
        Output → True
        
        Input → n = 10
        Output → False
    """
    pass



def custom_sort(words: List[str]) -> List[str]:
    """
    Sort list of strings by length first, then lexicographically.
    
    Example:
        Input → words = ["banana", "apple", "cherry", "date"]
        Output → ["date", "apple", "banana", "cherry"]
    """
    pass





if __name__ == "__main__":
    # You can use this section for testing your functions
    # Example:
    # print(sum_numbers(10))
    print(is_anagram("silent", "listen"))