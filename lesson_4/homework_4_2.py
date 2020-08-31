# FUNCTIONS

# Difference
# Write a function, which will calculate the difference of these two numbers
from random import random


def difference(num_1, num_2):
    diff = num_1 - num_2
    return diff


# Division
# Write a function, which will divide these two numbers

def division(num_1, num_2):
    return num_1 / num_2


# Function gets random number. If this number is more than ten, return the difference between 100 and this number,
# otherwise return this number multiplied by 10

def function_1(number):
    number = 3  # random.randint(1, 10)
    if number > 10:
        return 100 - number


# Your function temerature_convertor gets the temperature in Fahrenheit, convert it to Celsius and return.
# Formula (32°F − 32) × 5/9 = 0°C

def temerature_convertor(fahrenheit_degree):
    Celsius = (fahrenheit_degree - 32) * 5/9
    return Celsius


# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# as its only result rounded by 2 digits. Write a program that demonstrates the function.

def taxi_fare(distance):
    total_fare = round(((distance*1000/140)*0.25)+4, 2)
    return total_fare


# def taxi_fare(distance):
    # total_fare = float((distance*1000/140)*0.25+4)
    # result0 = str(total_fare)  # )
    # result = float(result0[0:6])
    # return round(result, 2)


# examples of usage:
# taxi_fare(10) #21.86
