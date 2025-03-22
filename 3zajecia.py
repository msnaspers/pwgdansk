def main() -> int:
    print("fff")

if __name__ == '__main__':
    pass
#wyonaj main z tego modulu tylko, bardziej jako entry point np w docker

def do():
    global suma 
    suma = 4+5

def a():
    do()
    print(suma)

a()


def pole(a,h):
    return a*h/2
def main():
    lis = [{"a":3,"h":5}, {"a":8,"h":12}, {"a":7,"h":4}]
    sum=0
    for e in lis:
        sum+=pole(e['a'],e['h'])
    print(sum)

#main()


def liczba(a: int) -> int:
    str_a=str(a)
    return str_a[len(str_a)-1:]

print(liczba(123577575478484))


'''a = reversed('123455666')
print(next(a))



for e in a:
    print(e)
    break'''

#indexy wsteczne -1,-2 znaki od konca


napis='kajak'

i=0

while i<=len(napis):
    i+=1
    print(napis[-i])

