"""
Create a Python program that checks if a given number is prime or not. The user
should input a number, and the program should print whether it is prime or not.
"""

def ask_number() -> int:
    """This functions ask the user to enter a integer number greater than 1

    Returns:
        int: the number entered by the user
    """
    while True:
        try:
            number = int(input("Enter a positive integer number, greater than 1: "))
            return number
        except ValueError:
            print("Invalid Input! Enter a integer number")

def is_prime(number: int) -> bool:
    """This function determines when a number is prime or not

    Args:
        number (int): a number given by the user

    Returns:
        bool: A bool that tells the user whether the number entered is prime or not
    """
    if number <= 1:
        return False
    
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
        
    return True

    
number = ask_number()

is_prime = print(is_prime(number))