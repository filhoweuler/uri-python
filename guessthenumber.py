import random

num = random.randint(1, 100)

guess = -1

guess_num = 10

while not guess == num:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("You should input a number!")
        continue
    
    if guess > num:
        print("Too high")
    elif guess < num:
        print("Too low")
    else:
        print("You won the game!")

    guess_num = guess_num - 1
        
