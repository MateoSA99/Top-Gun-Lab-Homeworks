"""
Create a Python function called reverse_string that takes a string as input and returns
the reversed string.
"""


def reverse_string(string: str) -> str:
    """A function that takes a string and then reverse it

    Args:
        string (str): string to reverse

    Returns:
        str: reversed string
    """
    reversed_string = string[::-1]
    return reversed_string

string = "Hello World!!"
print(reverse_string(string))

