# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == 'S':
    bill += 15
#   print('One Small Pizza: $15.')
    if add_pepperoni == 'Y':
        bill += 2
#       print('Peperonni for One Small Pizza: $2.')
if size == 'M':
    bill += 20
#    print('One Medium Pizza: $20.')
    if add_pepperoni == 'Y':
        bill += 3
 #       print('Pepperoni for One Medium Pizza: $3.')

if size == 'L':
    bill += 25
 #   print('One Large Pizza: $25.')
    if add_pepperoni == 'Y':
        bill += 3
 #       print('Pepperoni for One Large Pizza: $3.')
if extra_cheese == 'Y':
    bill += 1
 #   print('Extra Cheese: $1.')

print(f'Your final bill is: ${bill}')
