# # users = ["Chika", "Riko", "Emma", "Patrick", "Bethrand", "Lily", "John", "Alice", "Bob", "Charlie"]

# # print(len(users))

# # def wishHappyNewYear(user):
# #     print(f"Happy New Year, {user}!")

# # for user in users:
# #     wishHappyNewYear(user)



# number = 42
# max_trials = 5
# trial_count = 0

# print(max_trials > trial_count)

# while max_trials > trial_count: 
#     trial_count +=1
#     number_to_guess = int(input("Guess a number: "))

#     if number_to_guess < number:
#         print('guess is too low,try again')

#     if number_to_guess > number:
#         print('guess to high,try again')    

#     if number_to_guess == number:
#         print(f"You guessed it right, and it was {number_to_guess}")
#         break

#     if trial_count == max_trials :
# #         print("You have hit your limit")




# #A savings goal tracker
# #continually asks user to save up for a fixed goal(100)
# # fixed_goal_pt = 100
# # balance = 0

# # while fixed_goal_pt > balance:
# #     # balance += 1

# #     deposited_amount = int(input('Enter amount to be deposited: '))
# #     balance = balance + deposited_amount

# #     if balance < fixed_goal_pt:
# #         print('you are yet to reach your fixed goal' )

# #     if balance > fixed_goal_pt:
# #         print(f'you have reached your goal and is left with a remainder of {balance - fixed_goal_pt}')
# #         break

# #     if balance == fixed_goal_pt:
# #         print('you have raeched your fixed goal')
        
# ASSIGNMENT 1
# total_bil = 0

# while True:
        
#         item_price = input('Enter item price or type "done" to finish: ')
#         if item_price.lower() == 'done':
#             break
#         try:
#             item_price = float(item_price)
#             total_bil = total_bil + item_price
#         except ValueError:
#             print("Invalid input. Please enter a valid price.")

# print(f'Total bill amount: {total_bil}')




# #Dog Bus Tracker — Challenge Steps
# #
# # 1. Start with a bus dictionary holding current passengers.
# #    - Each seat number (1, 2, 3, ...) is a key
# #    - Each value is another dictionary with each pet's:
# #        • name
# #        • breed
# #        • pickup time
# #        • dropoff time
# #
# # 2. Print a starting roster showing each pet’s seat, name, and pickup time.
# #
# # 3. Add one new pet if there’s room on the bus.  
# #    - Use MAX_SEATS to limit capacity.  
# #    - Dynamically assign the next seat number.  
# #    - Print the updated roster showing all pets after pickup.  
# #
# # 4. Ask which pet leaves early.  
# #    - Remove that pet from the bus.  
# #    - Print a message saying they’ve headed home.  
# #
# # 5. Print a final roster listing the remaining pets and their dropoff times.


# max_seats = 4  
# bus = {
#     1: {"name": "Buddy", "breed": "Golden Retriever", "pickup_time": "8:00 AM", "dropoff_time": "5:00 PM"},
#     2: {"name": "Mittens", "breed": "Tabby Cat", "pickup_time": "8:15 AM", "dropoff_time": "5:15 PM"},
#     3: {"name": "Rex", "breed": "German Shepherd", "pickup_time": "8:30 AM", "dropoff_time": "5:30 PM"},
# }
# print("Starting Roster:")
# for seat, pet in bus.items():
#     print(f"Seat {seat}: {pet['name']} ({pet['breed']}) - Pickup: {pet['pickup_time']}, Dropoff: {pet['dropoff_time']}")

# max_seats = int(max_seats)

# if len(bus) < max_seats:
#     next_seat = len(bus) + 1
#     bus[next_seat] = {
#         "name": "Charlie",
#         "breed": "Beagle",
#         "pickup_time": "8:45 AM",
#         "dropoff_time": "5:45 PM",
#     }
# else:
#     print('no free seats')
# print("\nUpdated Roster:")
# for seat, pet in bus.items():
#     print(f"Seat {seat}: {pet['name']} ({pet['breed']}) - Pickup: {pet['pickup_time']}, Dropoff: {pet['dropoff_time']}")

# pet_to_leave = input("\nWhich pet leaves early? (Enter name): ")
# for seat, pet in bus.items():
#     if pet['name'] == pet_to_leave:
#         del bus[seat]
#         print(f"{pet['name']} has headed home.")
#         break
# else:
#     print("Pet not found.")

# print("\nFinal Roster:")
# for seat, pet in bus.items():
#     print(f"Seat {seat}: {pet['name']} ({pet['breed']}) - Pickup: {pet['pickup_time']}, Dropoff: {pet['dropoff_time']}")


# loops multiplication table


# ASSIGNMENT 2


while True:
    choice = input("Input A for the full multiplication table of a number, or input B to multiple or add or subtract or divide 2 integers: ")

    if choice.lower() == "a":
        print("You've selected choice A, so we're going to do a multiplication table of a number you input now")
        multiplication_number = int(input("Input the number you want us to provide the full multiplication table for"))
        for i in range(1, 13):
            print(f'{multiplication_number} * {i} = {i * multiplication_number}')
        break
    elif choice.lower() == "b":
        print("You've selected choice B, so we're going to do either addittion or subtraction or multiplication or division")
        first_number = int(input("Input the 1st number"))
        second_number = int(input("Input the 2nd number"))
        type_of_operation = input("Input the operation you want us to perform. 'Add', 'Minus', 'Divide', 'Multiply' ")

        if "add" in type_of_operation:
            print("You chose Addition.")
            print(f"Here's the addition of the 2 integers, {first_number + second_number}")
        elif "min" in type_of_operation:
            print("You chose Subtraction.")
            print(f"Here's the subtraction of the 2 integers, {first_number - second_number}")
        elif "div" in type_of_operation:
            print("You chose Division.")
            print(f"Here's the division of the 2 integers, {first_number / second_number}")
        else:
            print("You chose Multiplication.")
            print(f"Here's the multiplication of the 2 integers, {first_number * second_number}")
        break
    else: 
        print("You didn't input the right choice. Try again")
