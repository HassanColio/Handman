from words import palabras
import random

print("Welcome to the game hangman in Python")

def get_valid_word(palabras):
    word = random.choice(palabras)

    while '-' in palabras or ' ' in word :
        word = random.choice(palabras)

    return word

for i in get_valid_word(palabras):
    print (" _ ",end="")

print("")

    
