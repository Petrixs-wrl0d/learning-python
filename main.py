failed_subjects="2"
name='John'
print('Dear Mrs Badger')
print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
print(name + '  will need to redo ' + failed_subjects + '  courses.')
name="Eric"
print(name + '  is doing well in geography.')

item_name = 'widget'
price = 23.5
inventory = 100
is_in_inventory = False
print(item_name, price, inventory)

customer_name='patrick'
number_of_passes=10
tokens_per_pass=2
price_per_pass=20.00
tokens_per_game=2
total_tokens=number_of_passes * tokens_per_pass
total_cost=number_of_passes * price_per_pass
games_available=total_tokens//tokens_per_game
print("===== ARCADE DAY PASS =====")
print("Customer:", customer_name)
print("Passes:", tokens_per_game)
print("Tokens:", total_tokens)
print("Total Cost: $" + str(total_cost))

patient_name="patrick"
age=16
patient_arrival="2months"
print(patient_name)
print(age)
print(patient_arrival)
is_new=False

name = input('what is your name? ')
print('hi ' + name)
colour = input("what is your favourite colour? ")
print('you like colour ' + colour)
print(name +  ' likes' + colour)

numb1 = input('enter a number: ')
numb2 = input('enter another number: ')
print('the sum is: ' + str(int(numb1) - int(numb2)))


first_name = "Bethrand"
second_name = "Nnaemeka"

print("My name is " + first_name + " " + second_name)


print("a distance converter")
name = input('what is your name? ')
print('hello'  + name)
distance = input("what is the distance in km? ")
print('1m equals 1.609km')
print('distance in km,'  + distance + 'converted to miles is?') 
meters = distance * 1000
print('')


#INFINITE MENU CODE
def main():

    while True:
        print("\n--MENU--")
    print("1. Add an item")
    print("2. View backpack")
    print("3. quit")
    general = input('enter the option you wish to see: ')

    backpack = {item:qnty2
                }

    if general == "1":
        item = input("What item did you find? ")
        qnty = int(input("how many items were found? "))
        qnty2 = qnty
        backpack[item] = backpack.get(item, 0) + qnty2
        print(f"you added {qnty} + {item}(s) to your backpack")


    elif general =="3":
        print('goodbye')
        


    elif general == "2":
        if not backpack:
            print("your backpack is empty")
    else:
        print("your backpack contains: ")
        for item, qnty2 in backpack.items():
         print(f"{qnty2} {item}(s)")
    
if __name__ == "__main__":
    main()   