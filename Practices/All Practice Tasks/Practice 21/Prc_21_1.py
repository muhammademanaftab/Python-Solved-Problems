from random import *
def main():
    i=0    
    while i<=1:
        x=randint (1,9)
        y=randint (1,9)
        z=randint (1,9)        
        if x!=y or x!=z or y!=z:
            i=i+1
    print ('1st Number: ',x)
    print ('2nd Number: ',y)
    print ('3rd Number: ',z)
    
main()
