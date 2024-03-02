from random import *
def main():
    l=1
    while l<=10:
        l=l+1
        x=randint(1,100)
        y=randint(1,100)
        print (f'{x} or {y}')
        
        if x>y:
            print (x)
        else:
            print (y)
           
main()            
