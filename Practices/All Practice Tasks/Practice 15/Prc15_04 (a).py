from random import *

def main():
    i = 1
    min=9999999
    max=0
    while i <= 10:
        n1 = randint(1, 10000)
        n2 = randint(1, 10000)
        print ('N1: ', n1,    ' N2: ', n2)
        if i==1:
            max==i
            
        if n1>n2:
            n1,n2=n2,n1
        if n1<min:
            min=n1
        if n2>max:
            max=n2
        i=i+1
    print ('Max:  ',max, '\nMin:  ',min)

     

main()
