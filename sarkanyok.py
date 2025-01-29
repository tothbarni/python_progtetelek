import os
from colorama import Fore
os.system("cls")

def sarkany():
    f = 7
    m = 11
    ossz = 145
    for x in range(1, ossz // f + 1):
        maradek = ossz - x * f
        if (maradek > 0) and (maradek % m == 0):
            y = maradek // m
            if (y >= 1):
                print(f"{f} fejű sárkányok: {x}db  --  {m} fejű sárkányok: {y}db")

def sarkany2():
    y = 0
    f = int(input("\n1. Fejek száma: "))
    m = int(input("2. Fejek száma: "))
    ossz = int(input(f"{Fore.YELLOW}Összesen fejek száma: {Fore.RESET}"))
    for x in range(1, ossz // f + 1):
        maradek = ossz - x * f
        if (maradek > 0) and (maradek % m == 0):
            y = maradek // m
            if y >= 1:
                print(f"{f} fejű sárkányok: {Fore.GREEN}{x}db{Fore.RESET}  --  {m} fejű sárkányok: {Fore.GREEN}{y}db{Fore.RESET}")
    if y == 0:
        print(f"{Fore.RED}Nincs ilyen kombináció maradék nélkül!{Fore.RESET}")

sarkany()
sarkany2()
