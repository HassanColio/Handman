from words import palabras
import colorama
from colorama import Fore,init
init()
import random
colors = list(vars(colorama.Fore).values())

print("Bienvenidos al juego")


def good_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        return word

word = good_words(palabras)


for i in word:
    colored_chars = [random.choice(colors) + " _ "]
    print(" ".join(colored_chars),end="")

print("")