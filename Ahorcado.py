from words import palabras
import random

print("Welcome to the game hangman in Python")

def get_valid_word(palabras):
    word = random.choice(palabras)

    while '-' in palabras or ' ' in word :
        word = random.choice(palabras)

    return word

print(get_valid_word(palabras))

my_word = get_valid_word(palabras)
print (my_word+ '/n', len(my_word))

    
