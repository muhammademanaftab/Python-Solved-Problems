from random import *
def main():
    length=randint(5,15)
    x=[1]*length
    print('List:',end='')
    for i in range (length):
        x[i]=randint(0,9)
        print (x[i],end='  ')
    print()
    sort=0
    for i in range (length-1):
        if i==0 and x[i] < x[i+1]:
            sort=1
        elif x[i]<x[i+1] and sort==1:
            sort=1
        else:
            sort=0
    if sort==1:
        print ('List is sorted')
    else:
        print('List is not sorted')
main()
