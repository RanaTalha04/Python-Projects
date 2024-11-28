from data import MENU, resources

MONEY = 0
machine_stopped = False


def coin_processing(pennie, nickle, dimes, quarter):
    total_money = ((pennie * 0.01) + (nickle * 0.05) + (dimes * 0.10) + (quarter * 0.25))
    return total_money


while not machine_stopped:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "report":
        for key, val in resources.items():
            print(key,":", val)
        print(f"Money : ${MONEY}")
    
    elif user_input == "espresso":

        espresso_ingred = MENU["espresso"]["ingredients"]
        espresso_cost = MENU["espresso"]["cost"]

        for ingr_key, ingr_val in espresso_ingred.items():
            if resources[ingr_key] < ingr_val:
                print(f"Sorry, not enough {ingr_key}.")
                break
        else:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            total_coins = coin_processing(pennies, nickles, dimes, quarters)

            if total_coins < espresso_cost:
                print("Not enough money. Money refunded.")
            else:
                for ingr_key, ingr_val in espresso_ingred.items():
                    resources[ingr_key] -= ingr_val

                MONEY += espresso_cost
                change = round(total_coins - espresso_cost, 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
                print(f"Here is your {user_input} ☕. Enjoy!")

    elif user_input == "latte":
        
        latte_ingred = MENU["latte"]["ingredients"]
        latte_cost = MENU["latte"]["cost"]

        for ingr_key, ingr_val in latte_ingred.items():
            if resources[ingr_key] < ingr_val:
                print(f"Sorry, not enough {ingr_key}.")
                break
        else:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            total_coins = coin_processing(pennies, nickles, dimes, quarters)

            if total_coins < latte_cost:
                print("Not enough money. Money refunded.")
            else:
                for ingr_key, ingr_val in latte_ingred.items():
                    resources[ingr_key] -= ingr_val

                MONEY += latte_cost
                change = round(total_coins - latte_cost, 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
                print(f"Here is your {user_input} ☕. Enjoy!")

    elif user_input == "cappuccino":

        cappuccino_ingred = MENU["cappuccino"]["ingredients"]
        cappuccino_cost = MENU["cappuccino"]["cost"]

        for ingr_key, ingr_val in cappuccino_ingred.items():
            if resources[ingr_key] < ingr_val:
                print(f"Sorry, not enough {ingr_key}.")
                break
        else:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            total_coins = coin_processing(pennies, nickles, dimes, quarters)

            if total_coins < cappuccino_cost:
                print("Not enough money. Money refunded.")
            else:
                for ingr_key, ingr_val in cappuccino_ingred.items():
                    resources[ingr_key] -= ingr_val

                MONEY += cappuccino_cost
                change = round(total_coins - cappuccino_cost, 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
                print(f"Here is your {user_input} ☕. Enjoy!")
                
    elif user_input == "off":
        print("Machine powered off.")
        machine_stopped = True

    else:
        print("Wrong choice")
        machine_stopped = True
