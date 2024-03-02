from random import *
def main():
    i=1
    ha=0    
    has=0
    la=99999999
    las=99999999
    
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
            X=x
            Y=y
            Z=z

        if a<la:
            la=a
            las=i
            A=x
            B=y
            C=z
           
        i=i+1    
    print ('Highest Average set:  ',has)    
    print(f'Highest Average Elements:  {X}  {Y}  {Z}')
    print ('Lowest Average set:  ',las)    
    print(f'Lowest average Elements:  {A}  {B}  {C}')

main()
            
        
