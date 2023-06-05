import random

MIN_BET_SELECTION = 1
MAX_BET_SELECTION = 10
MIN_BET_AMOUNT = 1
MAX_BET_AMOUNT = 5000

wheel_numbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30,
                 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29,
                 7, 28, 12, 35, 3, 26]

number_colors = {
    0: 'Green',
    32: 'Red',
    19: 'Red',
    21: 'Red',
    25: 'Red',
    34: 'Red',
    27: 'Red',
    36: 'Red',
    30: 'Red',
    23: 'Red',
    5: 'Red',
    16: 'Red',
    1: 'Red',
    9: 'Red',
    7: 'Red',
    12: 'Red',
    3: 'Red',
    14: 'Red',
    18: 'Red',
    15: 'Black',
    4: 'Black',
    2: 'Black',
    17: 'Black',
    6: 'Black',
    13: 'Black',
    11: 'Black',
    8: 'Black',
    10: 'Black',
    24: 'Black',
    33: 'Black',
    20: 'Black',
    31: 'Black',
    22: 'Black',
    29: 'Black',
    28: 'Black',
    35: 'Black',
    26: 'Black',
}

       
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
    bet_mapping = {
        1: 'Red',
        2: 'Black',
        3: 'Even',
        4: 'Odd',
        5: 'Green'
    }

    print("Type '1' for Red.")
    print("Type '2' for Black.")
    print("Type '3' for Even.")
    print("Type '4' for Odd.")
    print("Type '5' for Green.")

    while True:
        bet_choice = input("Enter the number corresponding to your desired bet: ")
        if bet_choice.isdigit():
            bet_choice = int(bet_choice)
            if bet_choice in bet_mapping:
                return bet_mapping[bet_choice]
            else:
                print("Error: Invalid bet choice. Please enter a number from 1 to 5.")
        else:
            print("Error: Invalid input. Please enter a number.")



def get_bet_amount(choice):
    while True:
        bet_amount = input("How much do you wish to bet? €")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if 1 <= bet_amount <= MAX_BET_AMOUNT:
                return bet_amount
            else:
                print("Error: Invalid bet amount. Minimum bet is €1. Maximum bet is €5000.")
        else:
            print("Error: Invalid input. Please enter a number.")


def spin_roulette_wheel():
    print("Roulette wheel spinning...")
    print("No more bets.")
    winning_number = random.choice(wheel_numbers)
    winning_color = number_colors[winning_number]
    return winning_color, winning_number


def check_winnings(winning_color, winning_number, choice, stake):
    winnings = 0
    if winning_color == choice:
        print("Checking winning color")
        if winning_color == 'Red' or winning_color == 'Black':
            winnings = int(stake) * 2
        elif winning_color == 'Green':
            winnings = int(stake) * 15
    elif winning_number % 2 != 0 and choice == 'Odd':
        print("Checking if odd")
        winnings = int(stake) * 2
    elif winning_number % 2 == 0 and choice == 'Even':
        print("Checking if even")
        winnings = int(stake) * 2

    return winnings


while True:
    # Initial balance
    balance = add_money()
    print(f"Your balance is €{balance}")

    while True:
        # Get bet choice and amount
        choice = get_bet_choice()
        stake = get_bet_amount(choice)

        # Spin the wheel and determine the outcome
        winning_color, winning_number = spin_roulette_wheel()
        winnings = check_winnings(winning_color, winning_number, choice, stake)

        # Display the outcome and update the balance
        print(f"The ball has landed on {winning_color} {winning_number}")
        print(f"You bet €{stake}, and you won €{winnings}!")
        balance += winnings
        print(f"Your updated balance is €{balance}")

        # Check if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    # Check if the user wants to continue playing
    continue_playing = input("Do you want to leave the table? (yes/no): ")
    if continue_playing.lower() != "no":
        break

print('Your closing balance is: ', balance)