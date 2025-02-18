import random # importing random module
win = 0 # creating 3 variables and assign 0 to them outside the loop
lost = 0
rows = 0
while True: #create an infinite loop
    A = random.randint(1,3) # function that picks from min (1) and max (3)
    print(f"you  won {win} time\nlost {lost} times\nwon {rows} in a row") #shows user his status
    try: # try function, incase if error 
        player = int(input("\n\nChoose\n1-Rock\n2-Scissors\n3-Paper\nBy a number: ")) # input with integer data type
    except ValueError:# in result of vallues error
        print("Use numbers") #prints out instruction to user
        continue #repeats program from while loop
    if player == A: # if a number in input and number generated are same, it will be tie
        print("It's a tie!") # prints out tie
    elif player == 1 and A == 2: # 1 is rock and 2 is scissors. user pick rock and program scissors
        print("You win!") #prints out that user have won 
        rows += 1 #increament by 1 for both variable
        win += 1
    elif A == 1 and player == 2: # player pick scissors and program rock
        print("You lost") #lost message is printed out 
        lost += 1 # increment of lost
        rows = 0 # reassigned row variable if player lost the game
    elif player == 2 and A == 3: # scissors 2 and paper is 3. user picked scissors and program paper
        print("You win!")
        win += 1
        rows += 1
    elif A == 2 and player == 3: # player piscked paper and user picked scissors 
        print("You lost")
        lost += 1
        rows = 0
    elif player == 3 and A == 1: a# player piscked paper and program piscked rock
        print("You win")
        win += 1
        rows += 1
    else: # in this logic which is the last option, user picked a rock while program picked a paper
        print("You lost")
        lost += 1
        rows = 0
