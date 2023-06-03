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


def bet_type():
    while True:
        print("Type '1' Red.")
        print("Type '2' Black.")
        print("Type '3' Even.")
        print("Type '4' Odd.")
        print("Type '5' Green.")
        print('-=-=-=-=-=-=-=-=-=-=-')
        bet_selection = input("Choose the type of bet you wish to make: ")
        if bet_selection.isdigit():
            bet_selection = int(bet_selection)
            if 1 <= bet_selection <= MAX_BET_SELECTION:
                break
            else:
                print("Please enter a valid type of bet.")
        else:
            print("Please enter a number.")

    return bet_selection

add_money()
bet_type()