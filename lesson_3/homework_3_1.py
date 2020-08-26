# FOR LOOPS EXERCISES

# Ex. 1
# Enter your name, save it in name variable and save in result_1 variable your name repeated 3 times (use loops)

name_1 = None
result_1 = None

# TODO: Here is your code
name = input('Enter your name: ')
name_1 = name  # 'Jim'
count = 0
while count <= 3:
    result_1 = name_1 * count
    count += 1
print(result_1)

'''
def enter_name(name):
    name_1 = list(name)
    counter = 0
    while counter < 3:
        name_1.append(name)
        counter += 1
    result_1 = name_1[3:]
    return result_1

enter_name('Jim')
'''

# Ex. 2
# Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
# (save in variable number) and then save in result_2 variable your name repeated as many times as number_1 is
# (use loops)
name_2 = None
number_1 = None
result_2 = None

# TODO: Here is your code
name = input('Enter your name: ')
name_2 = name
number_1 = 6
while count <= number_1:
    result_2 = name_2 * count
    count += 1
print(result_2)

# Ex. 3
# Enter a random string, which includes only digits. Write code which find a sum of digits in this string and save it
# into result_3 variable

string_number_1 = None
result_3 = None

# TODO: Here is your code
string_number_1 = "47802398492038492842"
sum = 0
for char in string_number_1:
    if char.isdigit():
        sum += int(char)
result_3 = sum
print(sum)

# Ex. 4
# Create code which sums up all even numbers between 2 and 100 (include 100) and save it in result_4 variable

result_4 = None

# TODO: Here is your code
sum1 = 0
for i in range(2, 102, 2):
    if i % 2 == 0:
        sum1 += i
    result_4 = sum1
print(result_4)
