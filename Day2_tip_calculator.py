#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print('Welcome to Tip Calculator')

total = float(input('What is the bill total? \n$'))

party = int(input('How many members in your party?\n'))

percent = int(input('What percent tip would you like to give? 10, 12 or 15?\n'))

bill_total = percent / 100 * total + total

tip_total = (total / party) * (1 + (percent / 100))

tip_total = round(tip_total, 2)

message = f"Your total bill plus tip is ${bill_total} dollars and will be ${tip_total} per party member. Have a nice day."

print(message)
