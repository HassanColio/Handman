from words import palabras
from hangman import asciiArt
import colorama
from colorama import Fore,init
init()
import random
colors = list(vars(colorama.Fore).values())
vidas = 0
print("Bienvenidos al juego")


def good_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


word = good_words(palabras).upper()
word_list = list(word) #Separa lestras dentro de una list
count_letters = len(word_list) #Cant de letras a adivinar


while count_letters > 0 or vidas ==6:
    print("Guess the word or phrase")   
    for i in word_list:
        if i.isupper():
            colored_chars = [random.choice(colors)+ " _ " ]
            print(" ".join(colored_chars),end="")

        else:
            print(i,end="")

    print("")

    letter = input("\nLetter :").upper() 
    if letter.isalpha() and len(letter) == 1:
        cont = 0
        for i in range(len(word_list)):
            if letter == word_list[i]:
                word_list[i] = letter.lower()
                cont = cont + 1
        if cont == 0:
            vidas = vidas + 1
        else:
            count_letters = count_letters - cont

        print(asciiArt[vidas])
        if vidas == 6:
            print("Perdiste, la palabra era :")
            print(word_list)
            break

        if count_letters == 0:
            print("Ganaste")
            print(word_list)
    else:
        print("Caracter invalido, intenta de nuevo")
