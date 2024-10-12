print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_members = int(input("How many people to split the bill? "))

tip = total_bill + (total_bill * (percent_tip / 100))
split_bill = tip / split_members
print(f"Each person should pay: ${round(split_bill,3)}")
