# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

Ninety_yo_day = 90 * 365
Ninety_yo_weeks = 90 * 52
Ninety_yo_months = 90 * 12

day_age = int(age) * 365
week_age = int(age) * 52
month_age = int(age) * 12

days_left = Ninety_yo_day - day_age 
weeks_left = Ninety_yo_weeks - week_age
months_left = Ninety_yo_months - month_age


print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left")
