"""
Write a Python function called is_palindrome that checks if a given word is a
palindrome. The function should have proper error handling and be tested with
unittest.
"""

import unittest

def is_palindrome(word: str) -> bool:
    """Function that verify if a word is palindrome or not

    Args:
        word (str): word to verify if it is palindrome or no

    Returns:
        bool: True if word is palidrome or false if it is not
    """
    word = word.replace(" ", "").lower()
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

class PalindromeTest(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("May a moody baby doom a yam"))
        self.assertTrue(is_palindrome("Never odd or even"))
        self.assertTrue(is_palindrome("Do geese see God"))
        self.assertFalse(is_palindrome("Hello World"))
        self.assertFalse(is_palindrome("Maths are fun"))
        self.assertFalse(is_palindrome("God Bless U"))

if __name__ == "__main__":
    unittest.main()




    