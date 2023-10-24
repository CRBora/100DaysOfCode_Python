print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_num = int(input("How many people to split the bill? "))

tip = total_bill * tip_percentage / 100

price_per_person = (total_bill + tip) / people_num
final_price = round(price_per_person, 2)
#final_price = "{:.2f}".format(price_per_person)
print(f"Each person should pay: ${final_price:.2f}")
