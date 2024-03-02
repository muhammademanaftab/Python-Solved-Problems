from random import *
def main():
    x=[1]*10
    print ('Length:',(len(x)))
    sum=0
    for i in range (10):
        x[i]=randint(1,99)
        print (x[i],end='  ')
        sum=sum+x[i]
    print()
    average=sum//10
    print ('Average:',average)
    negative=0
    positive=0
    for i in range (10):
        diff=0
        diff= average - x[i]
        print (diff, end='  ')
        if average<x[i]:
            negative=negative+1
        else:
            positive=positive+1
    print ('Count of positive values:',positive)
    print ('Count of negative values:',negative)
main()
