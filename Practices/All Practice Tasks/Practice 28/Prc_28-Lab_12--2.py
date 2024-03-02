from random import *
def main ():
    x=[0]*10
    print('List: ',end='')
    for i in range (len(x)):
        x[i]=randint(1,9)
        print(x[i],end=' ')
    print()
    sum=0
    for i in range (len(x)):
        sum=sum + x[i]
    print('Sum:',sum)
main()