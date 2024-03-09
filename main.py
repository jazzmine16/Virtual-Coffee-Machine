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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




def is_resources_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"Sorry we are out of {item}")
            return False
    return True

def coins_process ():
    print("Please insert the coins-")
    total = int(input("How much quarter?? ")) * 0.25
    total += int(input("How much dimes ?? ")) * 0.1
    total += int(input("How much nickles?? ")) * 0.05
    total += int(input("How much pennies?? ")) * 0.01

    return total

def trancsaction_succesful (money_recieved , drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost )

        print(f"Here is your {change} change dear.")

        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry no sufficient money.")
        return False


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
        print(f"Here is your {drink_name}")

is_on =True

while is_on:
    choice = input("What do you like to have? Expresso , Cappuccino , Latte ").lower()
    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Milk : {resources['Milk']}ml")
        print(f"Money:${profit}")

    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = coins_process()
            if trancsaction_succesful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])







