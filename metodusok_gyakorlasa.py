import os

os.system('cls')
def Elso10SzamOsszege():
    osszeg = 0
    for i in range(0,11,1):
        osszeg += i
    return osszeg

def KettoSzamOsszegeKiirva(szam1:int, szam2:int):
    return szam1+szam2

def NegySzamOsszegeKiirva(szam1:int, szam2:int, szam3:int, szam4:int):
    return szam1+szam2+szam3+szam4

def HaromSzamOsszegenekGyokeKiirva(szam1:int, szam2:int, szam3:int):
    return ((szam1+szam2+szam3)**0.5)

def KiirKonzolra(szoveg:str, eredmeny):
    print(f"{szoveg}{eredmeny}")

o = Elso10SzamOsszege()
KiirKonzolra("Az első 10 szám összege: ", o)

a = KettoSzamOsszegeKiirva(10,15)
KiirKonzolra("Két szám összege: ", a)

b = NegySzamOsszegeKiirva(10,15,20,25)
KiirKonzolra("Négy szám összege: ", b)

c = HaromSzamOsszegenekGyokeKiirva(10,15,20)
KiirKonzolra("Három szám összegének gyöke: ", c)
