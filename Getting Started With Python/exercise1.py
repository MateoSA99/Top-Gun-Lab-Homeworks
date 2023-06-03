"""_
Writte a Python Program that takes two numbers as input from the user
and prints their sum
"""


def ask_numbers() -> float:
    """This function ask the user to input a number,
    if user enters a invalid input the program will ask to user for two numbers
    until he two valid inputs in a row

    Returns:
        float: this will be one of the two numbers to add
    """
    while True:
        try:
            number = float(input("Please Enter Your Number: "))
            return number
        except ValueError:
            print("¡Invalid Input. You must enter a number!")


def add_numbers(number1: float, number2: float) -> float:
    """This function adds two numbers

    Args:
        number1 (float): first number to add
        number2 (float): second number to add

    Returns:
        float: the sum of both numbers
    """
    result = number1 + number2
    return result


number1 = ask_numbers()
number2 = ask_numbers()

result = add_numbers(number1, number2)
print(f"The sum of {number1} and {number2} is: {result}")
