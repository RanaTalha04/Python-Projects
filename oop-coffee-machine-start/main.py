from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turned_off = False
coffee_report = CoffeeMaker()
coffee_menu = Menu()
money = MoneyMachine()


while not turned_off:
    menu = coffee_menu.get_items()
    user_input = input(f"What would you like? {menu}: ")

    if user_input == "off":
        print("Machine turned off")
        turned_off = True

    elif user_input == "report":
        report = coffee_report.report()
        print(report)

    else:
        drink = coffee_menu.find_drink(user_input)
        if coffee_report.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_report.make_coffee(drink)