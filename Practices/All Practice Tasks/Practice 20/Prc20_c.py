from random import *
def main(n):
    a=int(input('First Random Integer:  '))
    b=int (input ('Second Random Integer:  '))
    for i in range (n):
        c=randint(a,b)
        print (c,end=' ')
        
n=int(input('Count:  '))
main(n)
                
        
