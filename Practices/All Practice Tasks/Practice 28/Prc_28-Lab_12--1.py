from random import *
def main ():
    x=[0]*10
    print('List:',end='')
    for i in range (len(x)):
        x[i]=randint(1,9)
        print(x[i],end=' ')
    print()
    j=len(x)-1
    while j>=0:
        print (x[j],end=' ')
        j=j-1
main()