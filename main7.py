# Pizza Builder — Challenge Steps
#
# 1. Define a Pizza class that stores:
#    - size, crust type, and a list of toppings
# 2. Add a method to add a new topping
# 3. Add a method to remove a topping if it exists
# 4. Add a method to print pizza details:
#    - size, crust, and all toppings (or “No toppings yet!”)
# 5. Create a pizza object, customize it, and print the summary

class pizza:
    def __init__(self, size, crustType, toppings):
        self.size = size
        self.crustType = crustType
        self.toppings = toppings

    def add_topping(self, topping):
        self.toppings.append(topping)

    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)

    def print_details(self):
        print(f"Size: {self.size}")
        print(f"Crust Type: {self.crustType}")
        print(f"Toppings: {self.toppings}")
        if self.toppings:
            for topping in self.toppings:
                print(f"{topping}")
        else:
            print("  No toppings yet!")

# pizza_size = pizza('small', "thin", ['cheese', 'pepperoni']) 
# pizza_size.print_details()
n_size = input('enter size of the pizza: ')
n_crustType = input('enter crustType: ')
n_toppings = input('enter toppings seperated by a comma: ')
n_toppings = n_toppings.split(',')
my_pizza = pizza(n_size, n_crustType, n_toppings)
my_pizza.print_details()

print('YOUR PIZZA IS READY!!')
print(f'your pizza size is: {n_size} ')
print('your pizza crust is: ' + n_crustType)
print('your pizza toppings are: ' + ', '.join(n_toppings))


#assignment
# 1. Add an item 
# 2. view backpack
# # 3.quit
# choose an option: 2
# your backpack is empty!!
# --MENU--
# 1. Add an item 
# 2. view backpack
# # 3.quit
# choose an option: 1
# what item did you find?gold coin
# # how many?50
# # added 50 gold coin(s) to your backpack

# backpack = {}
# while True:
#         print("\n--MENU--")
#         print("1. Add an item")
#         print("2. View backpack")
#         print("3. quit")
#         general = input('enter the option you wish to see: ')

#         if general == "1":
#             item = input("What item did you find? ")
#             qnty = int(input("how many " + item + " were found? "))
#             qnty2 = qnty
#             backpack[item] = backpack.get(item, 0) + qnty2
#             print(f"added {qnty2} {item}(s) to your backpack")


#         elif general == "2":
#             if not backpack:
#                 print("your backpack IS empty ")
#             for item, qnty2 in backpack.items():
#                         print(f"your backpack contains: {qnty2} {item}(s)")
       
#         if general =="3":
#             print('goodbye')
#             break

# class dog:
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(f"{self.name} says woof")

# name = input("dog's name: ")
# my_dog = dog(name)
# my_dog.bark()