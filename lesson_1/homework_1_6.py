# Write your first program. Enter the temperature right now in Fahrenheit in temperature_fahrenheit variable as
# a string (e.g. '75') and convert it to Celsius.
# !important you should save only number to result_temperature. Formula (32°F − 32) × 5/9 = 0°C

# type your code here
temp_farenheit= input('Please enter the temp in farenheit ')
int(temp_farenheit)
result_temperature= (float(temp_farenheit)- 32) * 5/9
print ('The Temperature in celcius is ', result_temperature)
