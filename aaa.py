import random
lis=['zolty','czerwony','szary']
a=3
for e in range(a):
   
    random.shuffle(lis)
   
    print(f"Gosc {e+1}: {lis[0]}")
    del lis[0]
