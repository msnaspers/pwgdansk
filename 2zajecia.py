import numpy as np
import math as m
import random as r

a = r.randint(1,6)

b=  r.randint(1,6)

print(a,b,a+b)
def a(n:int):

    yield n
    yield n+1
gen = a(1)   
next(gen)

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
a=infinite_sequence()
print(next(a))
