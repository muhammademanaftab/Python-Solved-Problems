from random import *
def main ():
    x=[0]*10
    print('List: ',end='')
    for i in range (len(x)):
        x[i]=randint(1,9)
        print(x[i],end=' ')
    print()
    y=[]
    for i in range (len(x)):
        y.append(x[i])
    print('Copy of List: ',end='')
    for i in range (len(y)):
        print (y[i],end=' ')
main()