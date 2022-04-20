# This dictionary is the menu of the coffee machine. It contains 'espresso', 'latte', and 'cappuccino'. Each of these
# drinks also has its own dictionary of ingredients and a separate key/value of its cost.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# This resources dictionary is the amount of the ingredients that the machine has to work with. These numbers go down
# depending on which drink is ordered and can be completely depleted, making the machine unable to provide the ordered
# drink.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def use_resources(user_command):
    """
This 'use_resources()' function will check to make sure the machine has the resources needed to make the user's drink
choice. If there aren't enough ingredients, then the apology is printed and the drink is not made. If there are
enough ingredients then each of the ingredients the drink needs is subtracted from the machine's stores.
    :param user_command: string
    :return: boolean
    """
    global MENU
    global resources
    for ingredient in MENU[user_command]['ingredients']:
        if resources[ingredient] < MENU[user_command]['ingredients'][ingredient]:
            print(f"Sorry, there isn't enough {ingredient}.")
            return False
        else:
            resources[ingredient] -= MENU[user_command]['ingredients'][ingredient]
    return True



def drink_choice(command, inserted_money):
    """
This 'drink_choice()' function makes sure the user puts in enough coins for their choice. If they didn't, then the
machine refunds all the user's money. If the user put in enough money, and there are enough ingredients left inside
the machine then the machine makes the drink and puts the price of the drink into it's money store, refunding the user
any remaining money.
    :param command: string
    :param inserted_money: float
    :return: float
    """
    global MENU
    formatted_cost = "{:.2f}".format(MENU[command]['cost'])
    cost = float(formatted_cost)

    if user_payment < cost:
        print("Sorry, that's not enough money. Money refunded.")
        print("\n")
        return 0.00
    elif user_payment >= cost:
        if not use_resources(command):
            return 0.00
        else:
            user_change = "{:.2f}".format(inserted_money - cost)
            print(f"Here is ${user_change} of change.")
            print(f"Here is your {command}. Enjoy!")
            print("\n")
            return cost



money = 0.0
coffee_machine_on = True
espresso_cost = "{:.2f}".format(MENU['espresso']['cost'])
latte_cost = "{:.2f}".format(MENU['latte']['cost'])
cappuccino_cost = "{:.2f}".format(MENU['cappuccino']['cost'])


# Letting the user know they can turn off the coffee machine if they are done using it. Also, showing them the drink
# menu so that they know which drinks they can get and how many coins they should put into the machine.
print("This coffee machine is on. Type 'off' once you've had your fill of caffeine.")
print("Here is the drink menu:")
print(f"Espresso: ${espresso_cost}\nLatte: ${latte_cost}\nCappuccino: ${cappuccino_cost}")
print("\n")


while coffee_machine_on:
    # While the coffee machine is still on, the user will be able to see the resources the machine has left and how much
    # they have spent on drinks so far. The machine will also keep asking them which drink they want next.
    formatted_money = "{:.2f}".format(money)
    print(f"The machine is stocked with {resources['water']}ml of water, {resources['milk']}ml of milk, "
          f"and {resources['coffee']}g of coffee.")
    print(f"Money deposited in the machine: ${formatted_money}")
    print("\n")
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # If the user types 'off' then the machine will be turned off, but if they enter a valid choice then they will be
    # expected to input their coins and the 'drink_choice()' function will be activated to determine if the user can
    # get their drink or not.
    if user_choice == 'off':
        coffee_machine_on = False
    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        print("Please insert coins.")
        quarters = float(input("How many quarters: ")) * 0.25
        dimes = float(input("How many dimes: ")) * 0.10
        nickels = float(input("How many nickels: ")) * 0.05
        pennies = float(input("How many pennies: ")) * 0.01
        # Adding together the coins the user put into the machine.
        user_payment = quarters + dimes + nickels + pennies
        # Either 0.00 or the cost of the drink will be returned and added to the money stored in the machine.
        money += drink_choice(user_choice, user_payment)
    else:
        # If anything other than the valid commands are entered then this will print.
        print("Command unknown.")