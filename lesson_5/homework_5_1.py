# FOR LOOPS EXERCISES

# Enter your name, save it in name variable and create function print_name_three_times which return value is equal to
# your name three times

name_1 = 'Jimmy'


def print_name_three_times(name):
    if name == name_1:
        return name*3
    # pass


# Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
# (save in variable number) and then display their name that number of times. Each time add your name to result
# variable

name_2 = 'Jimmy'
number_1 = 10


def print_name_number_times(number, name):
    if name == name_2:
        count = 0
        result = ''
        while count < number:
            result = result + name
            count += 1
        return result
    #pass


# Enter a random string, which include only digits. Write function sum_digits which find a sum of digits in this string
# and save it in

string_number_1 = '4324376375383723296'


def sum_digits(string):
    sum0 = 0
    for char in string:
        if char.isdigit():
            sum0 += int(char)
    return sum0
    #pass


# Create function which sum up all even numbers between 2 and 100 (include 100)

def sum_even_numbers():
    sum1 = 0
    count = 0
    for i in range(2, 102, 2):
        if i % 2 == 0:
            sum1 += i
    return sum1
    #pass
