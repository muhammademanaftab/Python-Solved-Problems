from random import *
def main():
    i=1
    ha=0
    
    has=0
    while i<=10:
        x=randint(1,100)
        y=randint(1,100)
        z=randint(1,100)
        print (f'{x}  {y}  {z} ',end =' ')
        a=(x+y+z)//3
        print (a)
        print()
        if a>ha:
            ha=a
            has=i
            
        i=i+1    
    print (has)

main()
            
        
