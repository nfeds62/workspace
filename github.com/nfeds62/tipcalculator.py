print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip = total_bill * (tip_percentage / 100)
total_bill_with_tip = total_bill + tip
bill_per_person = total_bill_with_tip / people
final_amount = round(bill_per_person, 2)

if people == 1:
    print(f"Total bill: ${total_bill_with_tip}")
    print(f"Tip: ${tip}")
else:
    print(f"Each person should pay: ${final_amount}")

