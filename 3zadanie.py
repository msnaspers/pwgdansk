import random

a=int(input("Ile osob"))

kolory={1:"zolty",2:"niebieski",3:"szary"}




for e in range(1,a):
    kolor=kolory[random.randint(1,3)]
    print(e,kolor)




lista_kolorow=[]


a=input("liczba")

def mnozenie(liczba):
    wynik=liczba
    for e in range(1,10):
        wynik=wynik*e

print(mnozenie(a))






