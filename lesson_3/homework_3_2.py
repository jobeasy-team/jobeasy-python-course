# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = 'It is a random string in a variable'
char_1 = 'a'
result_1 = string_1.count(char_1)
print(result_1)


# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.
result_2 = 1
number_1 = int("2345")
while number_1 > 0:
    rem = number_1 % 10
    result_2 = result_2 * rem
    number_1 = int(number_1/10)
print(result_2)



# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = int("1234")
#result_3 = number_2[::-1]
result_3 = ''
while number_2 >0:
    rem = number_2 % 10
    result_3 = result_3 + str(rem)
    number_2 = int(number_2/10)
print(result_3)