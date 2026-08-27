print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much percent tip would you like to give? 10, 12, or 15? "))
split_by_people = int(input("How many people to split the bills?"))
tip_percentage_amt = tip_percentage /100
amount_post_split = round((total_bill + (total_bill * tip_percentage_amt))/split_by_people, 2)

print(f"Each Person Should Pay: ${amount_post_split}")
