from random import *
def main():
    i=1
    while i<=10:
        x=randint(1,100)        
        if i==1:
            i=i+1
            b=x        
        elif x==b+3 or x==b+2:
            i=i+1
            print (x,end='  ')
            b=x
            
main()

