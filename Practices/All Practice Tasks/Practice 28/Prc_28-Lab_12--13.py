from random import * 
def main ():
    x=[0]*10
    for i in range (len (x)):
        x[i]=randint(3,7)
        print(x[i],end=' ')
    print()
    for i in range (len(x)-2):
        for j in range (i,i+3):
            print (x[j],end=' ')
        print()
main()