"""
Create a Python decorator called timer that measures the time taken to execute a
function. Use this decorator on a function that sorts a list of random numbers and
prints the sorted list.
"""
import time
from typing import List

def timer_decorator(func):
    def wasted_time(*args, **kwargs):
        initial_time = time.time()
        execution = func(*args, **kwargs)
        final_time = time.time()
        total_time = final_time - initial_time
        print(f"the function took {total_time:.6f} seconds to execute")
        return execution
    return wasted_time

@timer_decorator
def sort_list(numbers: List[float]):
    """a Function that print a list of numbers but the list is in ascending order and
    calculates the  time it takes to run

    Args:
        numbers (List[float]): list of numbers
    """
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)


sort_list([2,3,4,5,6,7])

