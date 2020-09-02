# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write function counter, which will count how many times your character is included in your string

string_1 = ('d', 123, 'task', 's')
char_1 = 's'


def counter(string, char):
    count = 0
    for item in string:
        if item == char:
            count += 1
    return count


# Enter a random number and save it in variable number_1. Then create a function number_multiplication
# that will multiply all the digits together and return the result.

number_1 = 123


def number_multiplication(number):
    numbers = str(number)
    length = len(numbers)
    multiplied: int = 0
    count = 0
    while count < length:
        multiplied *= int(numbers[count])
        count += 1
    return multiplied


# Enter a random number and save it in variable number_2. Then create function number_reverse which will return
# a number with digits of number_1 in reverse order

number_2 = 4321


def number_reverse(number):
    num_str = str(number)
    digit = len(num_str) - 1
    res_num = ''
    while digit >= 0:
        res_num += num_str[digit]
        digit -= 1
    return int(res_num)
