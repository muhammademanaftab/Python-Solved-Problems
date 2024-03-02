from random import *
def main():
    length=randint(5,15)
    x=[1]*length
    y=[1]*length
    print('List 1:',end='')
    for i in range (length):
        x[i]=randint (0,100)
        print (x[i],end='  ')
    print()
    print ('List 2:',end='')
    for i in range (length):
        y[i]=randint(0,100)
        print (y[i],end='  ')
    print()
    for i in range (length):        
        if y[i]<x[i]:
            x[i],y[i]=y[i],x[i]
    print ('List 1:',end='')
    for i in range (length):
        print (x[i],end='  ')
    print ()
    print ('List 2:',end='')
    for i in range (length):
        print (y[i],end='  ')
        
main()
    
        
