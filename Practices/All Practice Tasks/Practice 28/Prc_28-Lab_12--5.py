from random import *
def main():
    x=[0]*10
    print('List: ',end='')
    for i in range (len(x)):
        x[i]=randint(1,9) 
        print (x[i],end=' ')
    print()
    even=0   
    print('Even: ',end='')
    for i in range (len(x)):
        if x[i]%2 == 0:
            even=even+1
            print (x[i],end=' ')
    print()
    odd=0   
    print('Odd: ',end='')
    for i in range (len(x)):
        if x[i]%2 != 0:
            odd=odd+1
            print (x[i],end=' ')
    print()
    print("Overall: ",end='')
    if even>odd:
        for i in range (len(x)):
            if x[i]%2 != 0:
                x[i]=x[i]+1
    if odd>even:
        for i in range (len(x)):
            if x[i]%2 == 0:
                x[i]=x[i]-1
    for i in range (len(x)):
        print (x[i],end=' ')
main()    