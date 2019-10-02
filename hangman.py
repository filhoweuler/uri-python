import random
import os

def game():
    words = ["test", "fork", "knife", "shoes", "water", "melon", "computer"]

    lifes = 5
    word = random.choice(words) # pick an element from a iterable
    hits = 0
    word_size = len(word)
    display = "_" * word_size
    display = list(display)

    while hits < word_size:
        hit = False
        guess = input("Guess a letter from the word: ").lower()
        for i in range(0,word_size):
            if word[i] == guess:
                hit = True
                hits = hits + 1
                display[i] = guess
        
        if not hit:
            lifes = lifes - 1
            if lifes == 0:
                print("You died! :(")
                print("The word was " + word)
                break

        print("".join(display))

    if not lifes == 0:
        print("You won!! :)")    

    

def main():
    while True:
        game()
        again = input("Play again? (y/n) ")
        if again != 'y':
            break

main()