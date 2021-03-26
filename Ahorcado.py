from words import palabras
from hangman import asciiArt
import colorama
from colorama import Fore,init
init()
import random
import os
colors = list(vars(colorama.Fore).values())



def good_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


word = good_words(palabras).upper()
word_list = list(word) #Separa letras metiendolas en una lista
count_letters = len(word_list) #Cant de letras a adivinar

vidas = 0
while count_letters > 0 or vidas == 0:
    
    print("Veremos si puedes adivinar la palabra 🤔")   
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

        print(asciiArt[vidas])   #RECORRER LA LISTA USANDO ITERADOR PARA EL MONITO
        if vidas == 6:
            os.system ("cls") #Limpiar pantalla
            print("Perdiste 👀, la palabra era :")
            print(word_list)  # Imprimir la palabra que era correcta
            break

        if count_letters == 0:
            os.system ("cls") # limpiar pantalla
            print("Ganaste 🎿 ")
            print(word_list)   # Imprimir la palabra
            
    else:
        print("Caracter invalido, intenta de nuevo")
