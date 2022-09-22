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


# todo print the report
# todo check the resource sufficient or not
def is_resource_sufficient(order_value):
    """Check if the resources are enough or not"""
    for i in order_value:
        if order_value[i] > resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True


# todo process coin
def coin_process():
    """Calculate the total value of coin"""
    total = int(input("How many Quarter : ")) * 0.25
    total += int(input("How many dimes : ")) * 0.10
    total += int(input("How many nickel : ")) * 0.05
    total += int(input("How many penny : ")) * 0.01
    return total


# todo check transition successful or not if yes then give them return
def is_transition_successful(money_got, drink_cost):
    """return the true if the payment is successful and false if
    payment is not successful"""
    if money_got >= drink_cost:
        change = round(money_got - drink_cost, 2)
        print(f"Here is your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("You don't inserted the enough coins")
        return False


# todo make coffee

def make_coffee(drink_name, order_value):
    """deduct the required value from the resources"""
    for item in order_value:
        resources[item] -= order_value[item]
    print(f"Here is your {drink_name}! enjoy")


is_on = True

while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino.): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"coffee : {resources['coffee']}g")
        print(f"Money : ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = coin_process()
            if is_transition_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
