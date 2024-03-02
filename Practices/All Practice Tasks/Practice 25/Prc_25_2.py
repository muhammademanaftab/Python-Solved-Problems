from random import *
def main():
    x=[1]*30
    sum=0
    for i in range (30):
        x[i]=randint(1,99)
        sum=sum+x[i]
        print (x[i],end='  ')
    average=sum//30
    print()
    print ('Average:',average)
    pas=0
    sum=0
    average_pass=0
    for i in range (30):
        if x[i]>50:
            pas=pas+1
            sum=sum+x[i]
    average_pass=sum//pas
    print ('Average of Pass Students:',average_pass)
    print ('Failed:',end=' ')
    for i in range (30):
        if x[i]<50:
            print (x[i],end='  ')
    print()
    print ('Above Average:',end=' ')
    for i in range (30):
        if x[i]>average:
            print (x[i],end='  ')
    print()
    print ('Below Average:',end=' ')
    for i in range (30):
        if x[i]<average:
            print (x[i],end='  ')
    print()             
main()