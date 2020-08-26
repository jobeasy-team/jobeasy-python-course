# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = "jdksdcklsdfisfuidhf"
char_1 = 's'
length = len(string_1) - 1
number_1 = 0
while length >= 0:
    if string_1[length] == char_1:
        number_1 += 1
    length = length - 1
    result_1 = number_1
print(number_1)

'''
#1
string_1 = "jdksdcklsdfisfuidhf"
char_1 = 's'
counter = 0
for char in string_1:
    if char == char_1:
        counter = counter + 1
result_1 = counter

#2
string_1 = "jdksdcklsdfisfuidhf"
char_1 = 's'
counter = 0
string_1_length = len(string_1) - 1
for i in range(string_1_length):
    if string_1[i] == char_1:
        counter += 1
    result_1 = counter

#3
string_1 = "jdksdcklsdfisfuidhf"
char_1 = "s"
result = string_1.count(char_1)
result_1 = result
'''


# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = 123
number_1s = str(number_1)
count = 0
mul = 0
while count < len(number_1s) - 1:
    mul *= int(number_1s[count])
    count += 1
    result_2 = mul

# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable
'''
number_2 = 123
number_1 = str(number_2)[::-1]
result_3 = int(number_1)
'''
number_2 = 123
number_2s = str(number_2)
number_1 = ''
length = len(number_2s) - 1
while length >= 0:
    number_1 = number_1 + number_2s[length]
    length = length - 1
    result_3 = int(number_1)
#print(result_3)

