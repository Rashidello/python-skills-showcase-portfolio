import random

#1 = rock, 2 = scissors , 3 = paper

while True:
    A = random.randint(1,3)

    try:
        player = int(input("Choose\n1-Rock\n2-Scissors\n3-Paper\nBy a number: "))
    except ValueError:
        print("Use numbers")
        continue
    
    if player == A:
        print("It's a tie!")
    elif player == 1 and A == 2:
        print("You win!")
    elif A == 1 and player == 2:
        print("You lost")
    elif player == 2 and A == 3:
        print("You win!")
    elif A == 2 and player == 3:
        print("You lost")
    elif player == 3 and A == 1:
        print("You win")
    else:
        print("You lost")
