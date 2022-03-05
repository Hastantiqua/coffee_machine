from data import MENU, resources


def get_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')


def is_enough_resources(user_choice):
    drink = MENU[user_choice]
    ingredients = drink['ingredients']

    for i in ingredients:
        if resources[i] < ingredients[i]:
            print(f'Sorry, there is not enough {i}.')
            return False
    return True


def calculate_total(user_choice):
    drink = MENU[user_choice]

    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))

    total = ((quarters * 0.25)
             + (dimes * 0.1)
             + (nickles * 0.05)
             + (pennies * 0.01))

    if total < drink['cost']:
        print('Sorry, that\'s not enough money. Money refunded.')
        return False

    change = total - drink['cost']
    if change != 0:
        print(f'Here is ${change:.2f} in change.')

    return True


def make_coffee(user_choice):
    drink = MENU[user_choice]
    ingredients = drink['ingredients']

    for i in ingredients:
        resources[i] -= ingredients[i]

    resources['money'] += drink['cost']

    print(f'Here is your {user_choice} ☕. Enjoy!')
    coffee_machine()


def coffee_machine():
    user_choice = input(
        '   What would you like? (espresso/latte/cappuccino): ').lower()

    if user_choice == 'off':
        return
    elif user_choice == 'report':
        get_report()
        coffee_machine()
    elif (user_choice == 'espresso' or
          user_choice == 'latte' or
          user_choice == 'cappuccino'):

        if is_enough_resources(user_choice):
            if calculate_total(user_choice):
                make_coffee(user_choice)
            else:
                coffee_machine()
        else:
            coffee_machine()

    else:
        print('Invalid choice. Please choose again.')
        coffee_machine()


coffee_machine()
