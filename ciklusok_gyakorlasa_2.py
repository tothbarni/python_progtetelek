import os
from colorama import Fore
os.system('cls')

valasz = input("Ismétlődhetnek a számok? i/n : ")

def ismetlodo():
    db = 0
    for i in range(2, 5):
        for j in range(2, 5):
            for k in range(2, 5):
                print(i, j, k)
                db += 1
    return db

def ism_nelkul():
    db = 0     
    for i in range(2, 5):
        for j in range(2, 5):
            for k in range(2, 5):
                if (i != j and j != k and i != k):
                    print(i, j, k)
                    db += 1
    return db

if (valasz == "i"):
    db = ismetlodo()
    print(f"{Fore.GREEN}{db}db{Fore.RESET} ilyen kombináció van.")
elif (valasz == "n"):
    db = ism_nelkul()
    print(f"{Fore.GREEN}{db}db{Fore.RESET} ilyen kombináció van.")

