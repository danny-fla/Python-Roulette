# Python Roulette

This is a command-line Roulette game implemented in Python. The game simulates a roulette wheel and allows players to place bets on various outcomes, such as colours (Red or Black), odd or even numbers and specific numbers (Straight bets). Players can choose their desired bet type, place bet amount within range and spin the roulette wheel to determine the winning outcome. The game calculates the winnings based on the player's bet and displays the result.


# Contents

- [Objective](<#Objective>)
- [How to play](<#How-to-play>)
- [User Experience](<#user-experience-ux>)
     - [Site Aims](<#site-aims>)
     - [Flowchart](<#flow-chart>)
- [Features](<#features>)
- [Future Features](<#future-features>)
- [Technologies Used](<#technologies-used>)
- [Testing](<#testing>)
    - [Code Validation](<#code-validation>)
    - [Lighthouse Testing](<#lighthouse-testing>)
    - [Responsive Testing](<#responsive-testing>)
    - [Manual Testing](<#manual-testing>)
- [Unresolved Bugs](<unresolved-bugs>)
- [Deployment](<#deployment>)
- [Disclaimer](<#disclaimer>)
- [Credits](<#credits>)
- [Acknowledgements](<#acknowledgements>)

# Objective

The aim of this project is to create an interactive Roulette game that provides the user with an enjoyable and realisitic gaming experience. The game should accurately simulate a roulette wheel, allow users to place different types of bets and provide feedback on the outcomes and winings.

# How to play

1. Run the "roulette_game.py" file in a Python environment.
2. The game will prompt you to deposit money into your account. Enter your desired amount to start playing.
3. Choose your bet type by entering the corresponding number: 
    - 1: Red
    - 2: Black
    - 3: Odd
    - 4: Even
    - 5: Green
    - 6: Straight (requires entering a specific number from 1 to 36)
4. Enter the amount you wish to bet, within the range allowed.
5. The roulette wheel will spin and the winning outcome will be displayed.
6. If you win, your balance will be updated with your earnings, otherwise it will deduct the amount of the bet placed.
7. At the end of each spin you will have the option to play again or leave the table.
8. When you decide to leave the table you will be informed of your closing balance amount.

# User Experience (UX)

## Site Aims
The primary aim of Python Roulette is to enterain users by offering a realisitic and engaging virtual gambling experience. The game should be easy to understand and navigate, allowing users to place bets effortlessly and enjoy the excitement of spinning the roulette wheel.

| ID | ROLE | EXPECTATIONS | TARGET |
|----|------|--------------|--------|
| 1  | User | As a player, I expect to deposit my money into my account before playing. | To allow me the opportunity to place money on a bet. |
| 2  | User | As a player, I expect the choice of choosing my desired type of bet and place said bet amount within the range allowed in the game. | Therefore allowing me the opportunity for flexibility. |
| 3  | User | As a player, I want to know if I won or lost the bet and see the winnings, if applicable. | To allow for transparency and feedback, it evaluates the effectiveness of my betting strategies. |
| 4  | User | As a player, I want to be able to play again or leave the table. | To allow for convenience and accessibility. |
| 5  | User | As a player, I want my account balance to be updated based on the outcome and winnings of each bet. | To allow for financial management. It provides essential information for decision-making, strategy development, and goal setting. |

## Flowchart

# Features

## RouletteGame class:

- The code defines a RouletteGame class that encapsulates the game logic and data. 
- It handles user interactions, manages the game state, and tracks the user's balance, betting history, and win statistics,

## User Interface:

- The code utilizes the art library to generate ASCII art for the game's welcome message.
- It also uses the colorama library to add color and style to the console output, enhancing the user experience.

## Game Initialization:

- Upon starting the game, the user is prompted to add money to their account by specifying the deposit amount.
- The entered amount is validated, and the balance is updated accordingly.

## Choosing type of bet:

- Asking players to choose their preferred bet type (Red, Black, Odd, Even, Green or Straight) improves their entertainment, offers customisation, provides strategic decision-making opportunities and adds variety to the gameplay experience.
- It allows players to place their bets with their personalized choices, gameplan or gut instinct which makes the game more captivating and engaging.

## Bet allowances:

- To promote fairness, financial planning and sensible gambling the game asks players to bet within the game's allowence.
- This ensures players' can allow for more decision-making, encourages risk manangement and adds to the game's balance.
- These boundaries creates a regulated environment for the player to safely enjoy the roulette experience.

## Spinning roulette wheel:

- Spinning the roulette wheel and finding out the winning outcomes provides excitment, spontanety, realisim and transparency for the user to enhances their engagment to the game.
- It gives clear feedback, ensures fairness and is an entertaining prcoess in the gameplay.
- This is an important part of the game as it add depth, excitement and originality to the roulette game experience.

## Winning calculations:

- Calculating and displaying winnings based on the bet and outcome of the roulette wheel spin gives the user feedback, provides them a reward and facilitates financial management.
- It gives the user a sense of satisfation and meaningness which further contributes to the game's enjoyability.

## Betting history tracking:

- After the end of each spin of the wheel the user's bet and stake along with the outcome of the bet is displayed to the user.
- This provides the user with a comprehensive overview of their betting activity throughout the game.

## Update account balance:
- This is crucial for allowing the user to make in-game decision, offers financial management and provides the user with fulfiment when they are successful. 
- They can then use this information to make informed choices based on their earnings or losses.

## Play again or leave table:
- By providing the option to play again or leave the table gives the user flexibility in making their decisions based on their convience, time and financial management.
- This makes sure that Python Roulette's appraoch is user-centered and offers a authentic experience to each player of the game.

# Future Features

- Implement different betting strategies for a more advanced gameplay.
- Add support for multiple players to join and allowing them to compete together.
- Include additional statistics and analysis of gameplay, such as win/loss ratio, winning streaks and other relevant data.
- Different roulette variations: Include support for different variations of roulette, such as European, American, or French roulette.

# Technologies Used
- Python Roulette was created using Python 3
# Testing

## Code Validation

## Lighthouse Testing


## Responsive Testing

## Manual Testing


| Action        | Expected           | Actual  |
| ------------- |:-------------:| -----:|
| Deposit money into the account | The account balance should update accordingly | Account balance is correctly updated |
| Deposit -€10 into the account | Display an error message stating that the deposit amount must be positive | Error message is displayed, preventing a negative deposit |
| Chose a bet type (e.g. Red, Odd) | The chosen bet type should be registered| Bet type is correctly registered |
| Chose a bet type by entering invalid type (e.g. letter, 7) | Display an error message indicating that an invalid bet choice was entered | Error message is displayed, informing the user about the invalid bet choice |
| Choose a straight bet and enter a number outside the range of 1-36 (e.g., 50) | Display an error message stating that the straight bet number is invalid | Error message is displayed, informing the user that the entered number is outside the valid range |
| Enter a valid bet amount within the allowed range | The bet amount should be accepted | The bet amount is accepted |
| Enter a bet amount of €1000 when the account balance is €500 | Display an error message indicating that the bet amount exceeds the account balance | Error message is displayed, informing the user that the bet amount is higher than the account balance |
| Spin the roulette wheel | The wheel should spin and land on random number and colour | The roulette wheel spins and successfully lands on a random number and colour |
| Check the bet outcome | Based on the outcome of the spin the game should determine if the bet is correct or incorrect | Outcome of the bet is correctly determined |
| Display winnings if bet is successful | If the bet wins the winnings should be displayed to user | Winnings are correctly displayed |
| Track and display betting history | The type of bet, user's stake and whether they won or lost should be displayed at the end of each spin | Betting history is correctly displayed |
| Option to play again or leave table is prompted |The player should have the option to quit the game of continue playing | The option to play or leave is correctly provided |
| Repeat the steps to play another round | The game should allow for multiple rounds of gameplay | Multiple rounds of gameplay is possible |
| Exhaust the account balance by repeatedly placing bets | Display a message indicating that the account balance is empty and prompt the user to add more money | Message is displayed, informing the user about the empty account balance and requesting to add more money |
| Verify the user's final balance upon exiting th game | The user's final balance should be correctly updated and displayed | The user's final balance is correctly displayed |


# Unresolved Bugs



# Deployment 


## To Fork a GitHub repository, follow these steps:


## To clone a GitHub repository, follow these steps.


# Disclaimer

This program is a gambling simulation and does not involve real money. It is intended for education and entertainment purposes only.

# Credits



# Acknowledgements


