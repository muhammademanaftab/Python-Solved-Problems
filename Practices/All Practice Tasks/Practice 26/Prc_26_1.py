from random import *
def main():
    length=randint(5,15)
    x=[1]*length
    for i in range (length):
        x[i]=randint (0,100)
        print (x[i],end='  ')
    print()
    print ('Pairs in Order:')
    for i in range (length-1):        
        if x[i]<x[i+1]:
            print (x[i],',',x[i+1])
main()
    
        
