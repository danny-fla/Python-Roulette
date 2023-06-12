import random
import time


class RouletteGame:
    MIN_BET_AMOUNT = 1
    MAX_BET_AMOUNT = 5000

    wheel_numbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30,
                     8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29,
                     7, 28, 12, 35, 3, 26]
    
    # Dictionary mapping numbers to their corresponding colors
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

    def __init__(self):
        self.balance = self.add_money()
        self.betting_history = []


    def add_money(self):
    # Function to prompt user to add money into their account
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


    def get_bet_choice(self):
    # Function to get the user's desired bet choice
        bet_mapping = {
            1: 'Red',
            2: 'Black',
            3: 'Odd',
            4: 'Even',
            5: 'Green',
            6: 'Straight'
        }

        print("Type '1' for Red.")
        print("Type '2' for Black.")
        print("Type '3' for Odd.")
        print("Type '4' for Even.")
        print("Type '5' for Green.")
        print("Type '6' for Straight")

        bet_choices = []

        while True:
            bet_choice = input("Enter the number corresponding to your desired bet: ")
            if bet_choice.isdigit():
                bet_choice = int(bet_choice)
                if bet_choice in bet_mapping:
                    if bet_mapping[bet_choice] == 'Straight':
                        while True:
                            straight_number = input('Enter the specific number (1-36) you want to bet on: ')
                            if straight_number.isdigit():
                                straight_number = int(straight_number)
                                if 1 <= straight_number <= 36:
                                    return f"Straight {straight_number}"
                                else:
                                    print("Error: Invalid straight number. Please enter a number from 1 to 36.")
                            else:
                                print("Error: Invalid input. Please enter a number.")
                    else:
                        return bet_mapping[bet_choice]
                else:
                    print("Error: Invalid bet choice. Please enter a number from 1 to 6.")
            else:
                print("Error: Invalid input. Please enter a number.")


    def get_bet_amount(self, choice):
    # Function to get the amount of money the user wants to bet
        while True:
            bet_amount = input("How much do you wish to bet? €")
            if bet_amount.isdigit():
                bet_amount = int(bet_amount)
                if self.MIN_BET_AMOUNT <= bet_amount <= self.MAX_BET_AMOUNT:
                    if bet_amount <= self.balance:
                        return bet_amount
                    else:
                        print("I'm sorry, you do not have enough in your account.")
                        print(f"You're balance is €{self.balance}")
                        add_more_money = input("Would you like to add more money? (yes/no): ")
                        if add_more_money.lower() == "yes":
                            deposit_amount = self.add_money()
                            self.balance += deposit_amount
                else:
                    print("Error: Invalid bet amount. Minimum bet is €1. Maximum bet is €5000.")
            else:
                print("Error: Invalid input. Please enter a number.")


    def spin_roulette_wheel(self):
    # Function to generate the game's winnging number and colour
        print("Roulette wheel spinning...")
        time.sleep(1)
        for _ in range(3):
            print("." * random.randint(3, 6))
            time.sleep(1)
        print("No more bets.")
        time.sleep(2)
        for _ in range(3):
            print("." * random.randint(3, 6))
            time.sleep(1)
        winning_number = random.choice(self.wheel_numbers)
        winning_color = self.number_colors[winning_number]
        return winning_color, winning_number


    def check_winnings(self, winning_color, winning_number, choice, stake):
    # Funciton to check if the user has won any money
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
        elif choice.startswith('Straight'):
            straight_number = int(choice.split()[1])
            if straight_number == winning_number:
                print("Checking if straight")
                winnings = int(stake) * 35

        return winnings


    def play_game(self):
        while True:
            choice = self.get_bet_choice()
            stake = self.get_bet_amount(choice)

            winning_color, winning_number = self.spin_roulette_wheel()
            winnings = self.check_winnings(winning_color, winning_number, choice, stake)

            print(f"The ball has landed on {winning_color} {winning_number}")
            if winnings > 0:
                print(f"Congratulations! You bet €{stake}, and you won €{winnings}!")
            else:
                print("Hard luck")
            
            self.balance += winnings
            self.balance -= stake
            print(f"Your updated balance is €{self.balance}")

            self.betting_history.append({
                "Bet": choice,
                "Stake": stake,
                "Win/Loss": "Win" if winnings > 0 else "Loss"
            })

            self.display_betting_history()

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break
    
    def display_betting_history(self):
        print("Betting history: \n")
        for bet in self.betting_history:
            print(f"Bet: {bet['Bet']}, Stake: €{bet['Stake']}, Result: {bet['Win/Loss']}")
        print()


    def play(self):
        while True:
            self.play_game()
            continue_playing = input("Do you want to leave the table? (yes/no): ")
            if continue_playing.lower() != "no":
                break

        print('Your closing balance is: € ', self.balance)
    

game = RouletteGame()
game.play()
