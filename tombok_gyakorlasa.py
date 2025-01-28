import random
import os
from colorama import Fore

os.system('cls')
def feltolt():
    lista = []
    for i in range(5):
        lista.append(1)
        rnd_szam = random.randint(0, 21)
        while (rnd_szam % 2 != 0):
            rnd_szam = random.randint(0, 21)
        lista.append(rnd_szam)
    return lista

def kiir(lista):
    print(lista)

lista = feltolt()
kiir(lista)