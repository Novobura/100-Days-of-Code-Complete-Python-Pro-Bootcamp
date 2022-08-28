#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print('Welcome to Tip Calculator')

total = input('What is the bill total? $\n')

party = input('How many members in your party?\n')

percent = input('What percent tip would you like to give? 10, 12 or 15?\n')

total = float(total)

party = float(party)

percent = float(percent)

tip_total = (total / party) * (1 + (percent / 100))

tip_total = round(tip_total, 2)

message = f"Your total bill plus tip is {tip_total} dollars per party member. Have a nice day."

print(message)
