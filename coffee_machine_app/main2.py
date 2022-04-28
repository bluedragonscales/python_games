# This version of the coffee machine is using OOP (object oriented programming).

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# The objects created from the classes that contain the methods and attributes needed for the program functionality.
coffee_menu = Menu()
coffee_report = CoffeeMaker()
money_exchange = MoneyMachine()

# So long as this variable is set to "True" then the machine will run.
coffee_machine_on = True

# This is the initial prompt so the user knows what the program is about and how to work it.
print("This coffee machine is on. Type 'off' once you've had your fill of caffeine. Print 'report' to "
      "see available resources")
print("Here is the drink menu:")
print(coffee_menu.get_items())
print("\n")

while coffee_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == 'off':
        # If the user enters "off" then the program will end.
        coffee_machine_on = False
    elif user_choice == 'report':
        # If the user enters "report" then there will be a report of the machine resources and the profit that it has
        # collected from the user's payments.
        coffee_report.report()
        money_exchange.report()
    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        # If the user enters any of the three drink choices the program will create an object of that drink item and get
        # that item's cost.
        drink_item = coffee_menu.find_drink(user_choice)
        drink_cost = coffee_menu.find_drink(user_choice).cost
        # If the user enters enough coins into the machine, and there is enough resources in the machine to make that
        # drink then the machine will make the drink and add the cost of the drink to the machine's profit. If either
        # of these conditions is false then the user's money will be refunded and will not be added to the machine's
        # profit.
        if coffee_report.is_resource_sufficient(drink_item):
            if money_exchange.make_payment(drink_cost):
                coffee_report.make_coffee(drink_item)
        else:
            print("Money refunded.")
    else:
        # If the user does not enter a command the machine is programmed for, then they will get this print message.
        print("Not a valid option.")
