import random

MIN_BET_SELECTION = 1
MAX_BET_SELECTION = 10
MIN_BET = 1


def add_money():
    while True:
        try:
            amount = int(input("How much would you like to deposit? €"))
            if amount > 0:
                break
            else:
                print("Minimum deposit is €1.")
        
        except ValueError:
            print("Please enter a valid number.")

    return amount


def get_bet_choice():
    print("Type '1' for Red.")
    print("Type '2' for Black.")
    print("Type '3' for Even.")
    print("Type '4' for Odd.")
    print("Type '5' for Green.")
    print("Type '6' for Straight.")

    while True:
        bet_choice = input("Enter the number corresponding to your desired bet: ")
        if bet_choice.isdigit():
            bet_choice = int(bet_choice)
            if 1 <= bet_choice <= 6:
                return bet_choice
            else:
                print("Error: Invalid bet choice. Please enter a number from 1 to 6.")
        else:
            print("Error: Invalid input. Please enter a number.")

# Example usage
add_money()
choice = get_bet_choice()
print("You chose:", choice)




