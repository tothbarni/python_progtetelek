from colorama import Fore
import os
os.system("cls")

def keres_allatok():
    for sertes in range(1, 101):
        for kecske in range(1, 101):
            juh = 100 - sertes - kecske
            if juh >= 1:
                teljes_kolteseg = 3.5 * sertes + (4 / 3) * kecske + 0.5 * juh
                if teljes_kolteseg == 100:
                    return sertes, kecske, juh 

eredmeny = keres_allatok()
if eredmeny:
    sertes, kecske, juh = eredmeny
    print(f"Sertésből: {Fore.YELLOW}{sertes}db{Fore.RESET}, Kecskéből: {Fore.YELLOW}{kecske}db{Fore.RESET}, Juhból: {Fore.YELLOW}{juh}db{Fore.RESET}")
else:
    print(f"{Fore.RED}Nincs megoldás{Fore.RESET}")