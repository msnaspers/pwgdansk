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



