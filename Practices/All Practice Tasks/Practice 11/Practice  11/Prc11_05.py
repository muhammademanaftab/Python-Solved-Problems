from random import *
def main():
    l=1
    E_sum=0
    O_sum=0
    while l<=10:
        l=l+1
        n=randint(1,100)
        print (f'Number: {n}')
        if n%2==0:            
            E_sum=E_sum+n
            
        else:
            O_sum=O_sum+n
           
    print (f'{E_sum} and {O_sum}')

main()        
