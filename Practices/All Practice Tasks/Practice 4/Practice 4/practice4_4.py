from random import *
def main():
    n1 = randint(1, 100000)
    n3 = randint(1, 100000)
    n2 = randint(1, 100000)
    n4 = randint(1, 100000)
    print ('Numbers before ordering')
    print (f'N1: {n1}\t\tN2: {n2}\t\tN3: {n3}\t\tN4: {n4}')
    if n1 > n2: n2, n1 = n1, n2;
    if n2 > n3: n2, n3 = n3, n2;
    if n3 > n4: n3, n4 = n4, n3;
    if n1 > n2: n2, n1 = n1, n2;
    if n2 > n3: n2, n3 = n3, n2;
    if n1 > n2: n2, n1 = n1, n2;
    print ('Numbers after ordering')
    print (f'N1: {n1}\t\tN2: {n2}\t\tN3: {n3}\t\tN4: {n4}')

main()
