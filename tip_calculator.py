# This tip calculator takes the total bill, divides it by the amount of people splitting it. Then it calculates the tip
# based off that divided portion and the tip percentage specified. After adding the tip to the divided portion, it
# prints the portion each person should pay.
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? = "))
people = int(input("How many people to split the bill? = "))

# First the tip is calculated by turning the percentage into a dollar amount (inside the parentheses) and then it adds
# that tip amount to the bill portion divided by the amount of people.
calculation = ((bill / people) * (tip / 100)) + bill / people

# This is a way to format a number so that even if it is a whole number, it will still end with 2 zeros.
each_person_pays = "{:.2f}".format(calculation)

print(f"Each person should pay: ${each_person_pays}")