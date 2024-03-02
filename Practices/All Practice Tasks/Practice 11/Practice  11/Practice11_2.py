from random import *

def main():
    i = 1
    while i <= 10:
        n1 = randint(1, 10000)
        n2 = randint(1, 10000)
        n3 = randint(1, 10000)
        print ('N1: ', n1, '\tN2: ', n2, '\tN3: ', n3)
        if n1 > n2: n1, n2 = n2, n1;
        if n2 > n3: n3, n2 = n2, n3;
        if n1 > n2: n1, n2 = n2, n1;
        print ('N1: ', n1, '\tN2: ', n2, '\tN3: ', n3,'\n')
        i = i + 1

main()
