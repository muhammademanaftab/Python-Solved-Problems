from random import *
def main():
    i=0
    while i<=1:
        x=randint (1,50)
        y=randint (1,50)
        if x+y==50:
            i=i+1
    print ('1st Number:  ',x)
    print ('2nd Number:  ',y)
main()
