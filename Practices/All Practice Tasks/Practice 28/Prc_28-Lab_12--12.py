from random import * 
def main ():
    x=[0]*10
    for i in range (len (x)):
        x[i]=randint(3,7)
        print(x[i],end=' ')
    print()
    for i in range (len(x)):
        sum=0
        for j in range (i+1):
            sum=sum+x[j]
            print (x[j],end=' ')
        print('=',sum)
main()