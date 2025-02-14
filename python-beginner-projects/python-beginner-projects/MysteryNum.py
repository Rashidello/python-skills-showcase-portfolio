import random
def difficulty():
    while True:
        try:
            max_numb = int(input("Pick maximum number: "))
            return max_numb
        except ValueError:
            print("Use numeric symbols")
            continue
def game(maximum_num):
    wins = 0 
    lose = 0
    row = 0
    while True:
        i = random.randint(1,maximum_num)
        print(f"You have {wins} wins, {lose} lost, and {row} wins in a row")
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            maximum_num = difficulty()
            continue
        if guess == i:
            print(f"You won!\nIt is {i}\n")
            wins += 1
            row += 1
        else:
            print(f"You lost!\nCorrect number is {i}\n")
            row = 0
            lose += 1
            continue
print("You can change diff any time by typing anything")
maximum_num = difficulty()
game(maximum_num)

