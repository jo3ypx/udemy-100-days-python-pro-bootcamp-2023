print("Welcome to the tip calculator.")
total_bill = input("What was the total bill?\n$")
percentage_tip = input(
    "What percentage tip would you like to give? 10, 12 or 15?\n")
number_people = input("How many people to split the bill?\n")
final_percentage = (int(percentage_tip) / 100) + 1
final_tip = round(float(total_bill) / int(number_people) * final_percentage, 2)
print("Each person should pay: $" + str(final_tip))
