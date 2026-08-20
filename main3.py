# #a function that converts kelvin to celsius
# def kelvin_to_celsius(kelvin_number):
#     celsiusVal = kelvin_number - 273.15
#     celsiusVal = round(celsiusVal, 2)
#     return celsiusVal

# kelvin = float(input("Enter temperature in Kelvin: "))

# celsiusValueForUser = kelvin_to_celsius(kelvin)

# print(f"{kelvin} Kelvin is equal to {celsiusValueForUser} Celsius.")



# mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
# num1 = float(input('Enter first number: '))
# if mode.lower() == 'f':
#     print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
# else:
#     num2 = float(input('Enter second number: '))

#     if mode == '+':
#         print(f'Answer is: {num1 + num2}')
#     elif mode == '-':
#         print(f'Answer is: {num1 - num2}')
#     elif mode == '*':
#         print(f'Answer is: {num1 * num2}')
#     elif mode == '/':
#         print(f'Answer is: {num1 / num2}')
#     else:
#         print('Input error!')

# def num_days(month):
    
#     month31 = ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']
#     month30 = ['apr', 'jun', 'sep', 'nov']
#     month28 = ['feb']

#     if month in month31:
#         print('number of days in',month,'is',31)
#     elif month in month30:
#         print('number of days in',month,'is',30)
#     elif month in month28:
#         print('number of days in',month,'is',28)
#     else:
#         print('invalid month')

# num_days(input('Enter month in short form: ').lower())

# from random import random


print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
#1. What do I want to repeat?
#  -> 
#2. What do I want to change each time?
#  -> 
#3. How long should we repeat?
#  -> 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
win = (numbers)
lose = 0
while lose < 5: 
    guess = input('Guess the number: ')
    if guess <= win:
        print('You win!')
        break
    elif guess < win:
        print('Your guess is too low.')
    elif guess > win:
        print('Your guess is too high.')
    lose += 1