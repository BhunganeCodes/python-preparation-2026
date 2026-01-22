def sum_numbers(n: int) -> int:
    """
    Return the sum of all numbers from 1 to n.
    
    Example:
        Input → n = 5  
        Output → 15  (because 1 + 2 + 3 + 4 + 5 = 15)
    """
    result = sum(i for i in range(1, n+1))
    return result


def reverse_list(lst: list) -> list:
    """
    Return a new list that is the reverse of the given list using a loop.

    Do not use Python’s built-in reverse().

    Example:
        Input → [1, 2, 3, 4, 5]
        Output → [5, 4, 3, 2, 1]
    """
    return lst[::-1]

def remove_duplicates(lst1: list) -> list:
    """
    Remove duplicate elements from the list while maintaining the order.

    Example:
        Input → [1, 2, 2, 3, 4, 4, 5]
        Output → [1, 2, 3, 4, 5]
    """
    result = []
    for n in lst1:
        if n not in result:
            result.append(n)
    return result

def fibonacci_series(n_terms: int) -> list:
    """
    Generate a Fibonacci series up to n terms.

    The series should start with 0, 1 and each term is the sum of the previous two.

    Example:
        Input → n_terms = 10
        Output → [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    result = []
    a, b = 0, 1

    if n_terms <= 0:
        return result
    
    if n_terms == 1:
        result.append(a)
        return result
    
    else:
        for _ in range(n_terms):
            result.append(a)
            a, b = b, a + b
    return result

def is_palindrome(s) -> bool:
    """
    Check if a given word or number is a palindrome.
    The function should accept either a string or an integer.

    - For strings, ignore spaces and case sensitivity.
    - For numbers, check if the digits read the same forwards and backwards.

    Example:

        Input → "Racecar", 121
        Output → True


    """
    return s.strip().lower() == s[::-1].strip().lower()



def char_frequency(s: str) -> dict:
    """
    Create a dictionary where keys are characters and values are the number 
    of times each character appears in the string.

    Example:
        Input → "hello world"
        Output → {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    """
    pass


def factorial(n: int) -> int:
    """
    Return the factorial of a given number.

    The factorial of n is n × (n−1) × (n−2) × ... × 1.
    If n = 0, return 1.
    Raise a ValueError if n is negative.

    Example:
        Input → n = 5
        Output → 120
    """
    pass


if __name__ == "__main__":
    # You can use this section for testing your functions
    # Example:
    # print(sum_numbers(10))
    print(sum_numbers(5))
    print(reverse_list([1, 2, 3, 4, 5]))
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
    print(fibonacci_series(10))
    print(is_palindrome("Racecar"))
