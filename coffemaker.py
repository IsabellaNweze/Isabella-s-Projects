
# COFFEE MACHINE PROJECT

logo = '''
                        (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   ""---...........---""   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           \ |                             |
           _/ /\                             /
          (/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.             .-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
      \\""--..                              __..--""/
       '._     """----.....______.....----"""     _.'
          ""--..,,_____            _____,,..--""
                        """----"""
'''

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0,
}


def isResouSuff(prompt):
    request = MENU[prompt]
    ingredients = request["ingredients"]
    coffee = resources["Coffee"] >= ingredients["coffee"]
    water = resources["Water"] >= ingredients["water"]
    milk = resources["Milk"] >= ingredients["milk"] 
    sufficent = coffee and water and milk 
    if not water:
        print("Sorry there is not enough water")
    if not coffee:
        print("Sorry there is not enough coffee")
    if not milk:
        print("Sorry there is not enough milk")
    return sufficent   
    

def ifTranSuc(prompt):
    '''  To print the result.
    and make the coffee request and deduct all the resources needed and add the cash to the resources.'''
    request = MENU[prompt]
    request_ingrdients = request["ingredients"]
    resources["Coffee"] -= request_ingrdients["coffee"]
    resources["Milk"] -= request_ingrdients["milk"]
    resources["Water"] -= request_ingrdients["water"]
    resources["Money"] += request["cost"]
    print(f"Here is your {prompt}. Enjoy! ")


def insertCoins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many penneis?: ")) * 0.01
    coins = [quarters, dimes, nickles, pennies]
    return sum(coins)


machineON = True
print(logo, "Weclome to Python Cafe☕️")
while machineON:
    error = True
    while error:
        prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if prompt == "espresso" or  prompt == "latte" or prompt == "cappuccino" or prompt == "off" or prompt == "report":
            error = False
        else:
            print("Oh sorry, We only have espresso, latte, cappuccino.")

    if prompt == 'off':
        machineON = False
        break

    if prompt == 'report':
        resource_values = f'''
        Water: {resources["Water"]}ml
        Milk: {resources["Milk"]}ml
        Coffee: {resources["Coffee"]}g
        Money: ${resources["Money"]}
        '''
        print(resource_values)

    else:
        if isResouSuff(prompt):
            cost = MENU[prompt]["cost"]
            print(f"The price of {prompt} is ${cost}")
            paid = insertCoins()

if paid >= cost:
                ifTranSuc(prompt)
                if not paid - cost == 0:
                    change = paid - cost
                    print(f"Here is ${round(change, 2)} in change")
                    
            else:
                print("Sorry that's not enough money. Money refunded. ")