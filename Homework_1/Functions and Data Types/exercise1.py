"""
Write a Python function called find_maximum that takes a list of numbers as input
and returns the maximum number from the list.
"""

from typing import List

def find_maximum(numbers: List[float]) -> float:
    """Function that takes a list of numbers and return its maximum

    Args:
        list (List[float]): list of number

    Returns:
        float: maximum of list
    """
    maximum = max(numbers)
    return maximum

print(find_maximum([1,2,4,5,6.8]))