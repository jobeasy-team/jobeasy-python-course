# FUNCTIONS

# Difference
# Write a function, which will calculate the difference of these two numbers

def difference(num_1, num_2):
    diff = num_1 - num_2;
    return diff

num_1 = 20
num_2 = 15
print("The difference is", difference(num_1,num_2))


# Division
# Write a function, which will divide these two numbers

def division(num_1, num_2):
    div = num_1 / num_2;
    return div

num_1 = 20
num_2 = 5
print("The division is", division(num_1,num_2))




# Function gets random number. If this number is more than ten, return the difference between 100 and this number,
# otherwise return this number multiplied by 10

def function_1(number):
    
    if number > 10:
        return(100 - number)
    else:
        return(100 * number)

number=int(input("input a random number : "))
print(function_1(number))
    

# Your function temerature_convertor gets the temperature in Fahrenheit, convert it to Celsius and return.
# Formula (32°F − 32) × 5/9 = 0°C

def temperature_convertor(fahrenheit_degree):
    return(float(fahrenheit_degree)-32) * 5/9

fahrenheit_degree= input('Please enter the temp in farenheit ')
print ('The Temperature in celcius is ', temperature_convertor(fahrenheit_degree))


# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# as its only result rounded by 2 digits. Write a program that demonstrates the function.

def taxi_fare(distance):
    tot_fare=round(10 * 1000 / 140 * 0.25 + 4, 2)
    return tot_fare
print
distance=int(input("please enter the distance in KM: "))
print('The total fare is : ',taxi_fare(distance))


# examples of usage:
# taxi_fare(10) #21.86
