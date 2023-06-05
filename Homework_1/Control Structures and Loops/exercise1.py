"""
Write a Python program that prints the first 10 Fibonacci numbers using a loop.
"""


def ask_number_elements() -> int:
    """This functions ask to the user to the number of elements in the fibonacci sequence
    that user wants to see

    Returns:
        int: the number entered by the user
    """
    while True:
        try:
            number = int(input("Please Enter Your Number: "))
            return number
        except ValueError:
            print("Invalid Input. You must enter a number!")


def fibonacci_sequence(number: int):
    """This function return the first numbers of the fibonacci sequence
    The number of elements that will be show is given by the user.

    Args:
        number (int): the number of terms of the fibonacci sequence that user wants to see
    """
    first_elements = [1, 1]
    if number == 1:
        return print(first_elements[0])
    else:
        for i in range(2, number):
            next_number = first_elements[i-1] + first_elements[i-2]
            first_elements.append(next_number)
    print(*first_elements)


number = ask_number_elements()

fibonacci_elements = fibonacci_sequence(number)
