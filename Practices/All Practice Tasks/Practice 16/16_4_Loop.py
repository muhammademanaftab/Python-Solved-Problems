from random import *
def main():
    m=int(input('Rows:  '))
    n=int(input('Columns:  '))
    for i in range (m):
        for j in range (n):
            x=randint(1,9)
            print (x,end=' ')
        print()
main()
