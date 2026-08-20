name = input('enter your name: ')
# # distance_km = input('enter a distance in km: ')
# # distance_m = float(distance_km) / 1.609
# # print('hey ' + str(name) + ' you travelled a distance of ' + str(round (distance_m,2)) + ' in miles' )
# # print('this the the users name ' + name + ' and the distance in km ' + distance_km)

# # msg='welcome to Python 101: Strings'

# # tyler1='tyler'

# # msg1=msg[18].title()

# # msg2 = msg[:7].title()

# # msg3 = msg[25:29].title()

# # mssge = msg1, msg2, msg3, 'to tyler'.title()
# # str_message = " ".join(mssge)[::-1]
# # print(str_message)




# wording = "Hello, python!"

# split_word = wording[::2]
# print(split_word)

# Ask a user for their favourite quote
# In this manner, print out the response

# # You're favourite quote is: Knowledge is power. And it containts 18 chars.
# quote = input('what is your favourite quote? ')
# print("your favourite quote is: " + quote + ' and it contains ' +str(len(quote)), "characters")

# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color.lower() + '!'
# msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
# print(msg)
# print(msg1)

# trace_time = float(input('what is the total race time in seconds? '))
# tpit_stop = int(input('how many pit stop were made? '))
# apit_stop = float(input('what is the average pit stop duration in seconds...'))
# total_pit_time = int(tpit_stop) * int(apit_stop)
# percentage_spent = int(total_pit_time) / int(trace_time) *100
# rounded_percentage = round(percentage_spent, 2)
# print("...pit stop summary...")
# print(f'total pit stop time: {total_pit_time} ')
# print(f'percentage_spent:{percentage_spent}% ')
# if rounded_percentage > 5: 
#     print("you need a new pit crew🚗")

def greeting(name, age=28, color='red'):
    #Greets user with 'name' from 'input box' and 'age', if available, default age is used
   print(f'Hello {name}, you will be {int(age) + 1} years old on your next birthday!')

name = input('Enter your name: ').capitalize()
age = input('Enter your age: ')
color = input('what is your fav colour? ').lower()
greeting(name, age, color)
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase 
print(f'we hear you like the colour {color}')

def greeting(name, age=28, color="red"):
 #Greets user with “name” from “input box” and “age”, if available, default age is used   
   print("Hello "  +  name.capitalize() + ", you will be " + str(age+1) +" next birthday!")
   print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
   print(f"We hear you like the color {color.lower()}!")

greeting("brian", 27,"Blue")
