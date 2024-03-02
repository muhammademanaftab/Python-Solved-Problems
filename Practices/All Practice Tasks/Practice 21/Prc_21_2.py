from random import * 
def main():
    i=0
    while i<=1:
        x=randint (2,20)
        y=randint (2,20)
        if y%x==0 :
            i=i+1
    print ('1st Number:  ',x)
    print ('2nd Number:  ',y)
main()
