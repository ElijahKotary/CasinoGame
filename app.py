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

