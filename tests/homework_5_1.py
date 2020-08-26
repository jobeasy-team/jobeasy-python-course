# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT
# PLEASE, DON'T CHEAT


# THIS FILE HAS ANSWERS. USE IT ONLY WHEN YOU HAVE SUCCESSFULLY PASSED HOMEWORK TESTS


from lesson_5.homework_5_1 import difference, division, function_1, temerature_convertor, taxi_fare
import pytest


def test_difference():
    # Difference
    # Write a function, which will calculate the difference of these two numbers
    if difference(10, 1) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert 10 - 1 == difference(10, 1)


def test_division():
    # Division
    # Write a function, which will divide these two numbers
    if division(2, 1) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert 2 / 1 == division(2, 1)


def test_function_1():
    # Function gets random number. If this number is more than ten, return the difference between 100 and this number,
    # otherwise return this number multiplied by 10
    if function_1(20) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert 100 - 20 == function_1(20)
    assert 5 * 10 == function_1(5)


def test_temerature_convertor():
    # Your function temerature_convertor gets the temperature in Fahrenheit, convert it to Celsius and return.
    # Formula (32°F − 32) × 5/9 = 0°C
    if temerature_convertor(10) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert (100 - 32) * 5 / 9 == temerature_convertor(100)


def test_taxi_fare():
    # Taxi Fare
    # In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
    # Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
    # as its only result rounded by 2 digits. Write a program that demonstrates the function.
    if taxi_fare(10) == None:
        pytest.skip(f"You didn't finish this task. the result variable equals None")
    assert taxi_fare(10) == round(10 * 1000 / 140 * 0.25 + 4, 2)
