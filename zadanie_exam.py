import random


kolory={1:"zolty",2:"niebieski",3:"szary",4:"rozowy"}
liczba_g=4


lis=[]
n=[]
for e in range(1,liczba_g+1):
    while 1==1:
        a=random.randint(1,4)
        if f'{kolory[a]}' not in n:
            break
    
    lis.append(f'{e} osoba:{kolory[a]}')
    n.append(f'{kolory[a]}')
print(lis)

