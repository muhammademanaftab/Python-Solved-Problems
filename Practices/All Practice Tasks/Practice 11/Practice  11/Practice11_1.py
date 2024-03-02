from random import *

def main():
    i = 1
    while i <= 10:
        n1 = randint(1, 10000)
        n2 = randint(1, 10000)
        print ('N1: ', n1, 'N2: ', n2)
        if n1 > n2: print ('First number is larger');
        else:       print ('Second number is larger');
        i = i + 1

main()
