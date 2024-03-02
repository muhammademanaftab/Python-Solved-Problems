from random import *
def main():
    n1 = randint(1, 10)
    n3 = randint(1, 10)
    n2 = randint(1, 10)
    print (f'N1: {n1}\t\tN2: {n2}\t\tN3: {n3}')
    d12 = n1 - n2
    d23 = n2 - n3
    d13 = n1 - n3
    if (d12 >=2 or d12 <= -2) and  (d12 >=2 or d12 <= -2) and  (d13 >=2 or d13 <= -2):
        print ('Ok')
    else:
        print ('Sorry')

main()
