"""
Create a Python program that converts a temperature from Fahrenheit to Celsius.
The user should enter the temperature in Fahrenheit, and the program should print
the equivalent temperature in Celsius.
"""

def ask_fahrenheit_temperature() -> float:
    """This function ask to the user to enter a valid temperature, if not
    the function will ask until he enters a valid temperature

    Returns:
        float: it is the temperature in fahrenheit that the user entered
    """

    while True:
        try:
            temperature = float(input("What is the temperature in Fahrenheit degrees?: "))
            return temperature
        except ValueError:
            print("¡Invalid Input. You must enter a valid temperature!")

def convert_to_celcius(fahrenheit_temperature: float) -> float:
    """This function converts a fahrenheit temperature in celcius temperature

    Args:
        fahrenheit_temperature (float): the fahrenheit temperature that will be converted 
        to celsius

    Returns:
        float: the converted temperature in celcius
    """
    celcius = round((fahrenheit_temperature - 32) * 5/9, 3)
    return celcius

fahrenheit_temperature = ask_fahrenheit_temperature()

celcius_temperature = convert_to_celcius(fahrenheit_temperature)

print(f'The Temperature {fahrenheit_temperature} Fahrenheit in Celcius is: {celcius_temperature}')