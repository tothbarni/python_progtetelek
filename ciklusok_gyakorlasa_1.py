import random
from colorama import Fore
import os

os.system('cls')
def vel_szam():
    i = 0
    szam = 0
    szamok = []
    while (szam != 13):
        szam = random.randint(10,15)
        szamok.append(szam)
        i += 1
    return i

index = vel_szam()
print(f"A {Fore.GREEN}{index}.{Fore.RESET} random szám lett 13.")

def lista():
    szamok = []
    i = 0
    while i < 20:
        szam = random.randint(10,15)
        if szam != 13:
            szamok.append(szam)
            i += 1
    return szamok

lista = lista()

def paros_osszegzes():
    db = 0
    osszeg = 0
    szam = 0
    while db < 10:
        if szam % 2 == 0:
            osszeg += szam
            db += 1
        szam += 2
    return osszeg

osszeg = paros_osszegzes()
print(f"Első 10 páros szám összege: {osszeg}")

def paratlan_osszegzes():
    db = 0
    osszeg = 0
    szam = 25
    while db < 38:
        if szam % 2 == 1:
            osszeg += szam
            db += 1
        szam += 2
    return osszeg

osszeg = paratlan_osszegzes()
print(f"Az első 38 db páratlan szám összege 24-től: {osszeg}")

def abs2():
    for i in range(-3, 4, 1):
        print(f"|{i*-1:2}| = {abs(i)}")

abs2()