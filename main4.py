# #QUADRATIC FORMULA CODE
# def quadratic_eqn(x,y,z) : 
#     sqrt1 = pow(y,2)-(4*x*z)
#     sqrt1 = sqrt1 ** 0.5

#     var1 = (-y + sqrt1)/2*x
#     var2 = (-y - sqrt1)/2*x
#     return var1,var2

# a = int(input('value for a? '))
# b = int(input('value for b? '))
# c = int(input('value for c? '))

# quadratic_eqn_answers = quadratic_eqn(a,b,c)

# print(quadratic_eqn_answers)







# 1. Set up two variables: one for total price, one for drink count
# 2. Start a while True loop
# 3. Ask for the customer's name
# 4. If the name is "done", break the loop
# 5. Ask for their drink order
# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 7. If it's not one of those drinks, print a warning and continue
# 8. After the loop, print total number of drinks and total price

total_price = 0
drink_count = 0

while True:
    customer_name = input("Enter your name (or 'done' to finish): ")
    if customer_name.lower() == 'done':
        break

    drink_order = input("Enter your drink order (latte/americano/espresso): ")
    if drink_order.lower() == 'latte':
        total_price += 3.50
        drink_count += 1
    elif drink_order.lower() == 'americano':
        total_price += 3.00
        drink_count += 1
    elif drink_order.lower() == 'espresso':
        total_price += 2.50
        drink_count += 1
    else:
        print("Invalid drink order. Please try again.")

print(f"Total number of drinks: {drink_count}")
print(f"Total price: ${total_price:.2f}")





# names = ['john ClEEse','Eric IDLE','michael']
# names1 = ['graHam chapman', 'TERRY', 'terry jones']

# for i in range(2):
#     name1 = input('what is your name? ')
#     names.append(name1)
    

# all_guests = names + names1

# for guest in all_guests: 
#     print(f'{guest.title()}! you are invited to the party on saturday.')



# us_number = input('Enter your US phone number: ')
# us_numb = us_number.strip()

# for ch in ['(', ')', '-', ' ']:
#     us_numb = us_numb.replace(ch, '')
    
# prts = us_numb.split()    
# digits = ''.join(prts)

# if len(digits) == 10:
#     area_code = digits[:3]
#     middle = digits[3:6]
#     last_four = digits[6:10]
#     print(f'Your phone number is: ({area_code}) {middle}-{last_four}')
# else:
#     print('error')    

# revoked_badges = {"B1319", "P2489", "E8003", "X7824", "W2345"}
# approved = []
# denied = []

# while True:
#     name=input('Enter your name or "done" to finish: ')
#     if name.lower() == 'done':
#         break
    
#     badgenumber = input('Enter your badge number: ').strip().upper()
#     if badgenumber in revoked_badges:
#         print(f'Sorry {name}, your badge number {badgenumber} has been revoked.')
#         denied.append(name)
#     else:
#         approved.append(name)
#         print(f'Welcome {name}, your badge number {badgenumber} is approved.')

# print('     Access Summary   ')       

# print('Approved visitors:')
# for name in sorted(approved):
#     print(f' - {name}')
# print('Denied visitors:')
# for name in sorted(denied):
#     print(f' - {name}')

# print(f'approved: {len(approved)}')
# print(f'denied: {len(denied)}')

print('loyalty points engine challenge')
print('one dollar = three points')
dollar = float(input('Enter the amount in dollars: '))

pts_in_dollar = 3.00 * dollar
print(f'you have {pts_in_dollar}')

bronze = 100
silver = 499
gold = 900 #500

tier_label = ('bronze' if pts_in_dollar < 100 else ('silver' if pts_in_dollar < 499 else 'gold'))
if pts_in_dollar < 100:
    print('your rank in pts is bronze')
elif pts_in_dollar >= 100 and pts_in_dollar < 499:
    print('your rank in pts is silver')
else:
    print('your rank in pts is gold')

print(f'total points earned: {pts_in_dollar}')
print(f'total points spent: {pts_in_dollar}')
print(f'final tier: {tier_label}')
