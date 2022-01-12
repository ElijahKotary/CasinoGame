import random

def rollIt():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    x = int(die1 + die2)
    print("Rolled a", x)
    return x

class game_info:    
    print("Lucky Roll")
    print("Rules are simple, your guess must equal the total of the two rolled dice.")
    print("------------------------------------------------------------------")
    print("Minimum bet is $5")
    print("Maximum bet is $10")
    print("------------------------------------------------------------------")

def total_bank(bank):
    bet = 0
    while bet <= 0 or bet > min([500,bank]):
        print(f"You have ${bank} in your bank.")
        a = input("Enter your bet ")
        bet = int(a)
    return bank,bet

def get_guess():
    guess = 0
    while (guess < 2 or guess > 12):
        try:
            guess = int(input("Choose a number between 2 and 12: "))
        except ValueError:
            guess = 0
        return guess

game_info()
bank = 500

while True:
    bank,bet = total_bank(bank)
    guess = get_guess()

    if guess == rollIt():
        bank += bet
        
    else:
        bank = bank - bet

    print(f'You have ${bank} in your bank.')
    print(f'Thanks for playing!\n')