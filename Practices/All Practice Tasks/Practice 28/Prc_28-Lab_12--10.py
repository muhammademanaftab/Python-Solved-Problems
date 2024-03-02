from random import * 
def main ():
    x=[0]*10
    for i in range (len (x)):
        x[i]=randint(3,7)
        print(x[i],end=' ')
    print()
    for i in range (len(x)):
        for j in range (x[i]):
            print ('*',end=' ')
        print()
main()