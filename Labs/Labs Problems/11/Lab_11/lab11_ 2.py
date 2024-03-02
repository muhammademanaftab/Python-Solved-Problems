from random import *
def main():
    x=[0]*30
    length=30
    print ('Marks:',end='')
    for i in range (length):
        x[i]=randint(0,100)
        print (x[i],end=' ')
    print ()
    y=[0]*30
    for j in range (length):
        y[j]=j+1
    for k in range (randint(3,5)):
        y[randint(0,29)]=-1
    print ('Roll No: \t\t Marks')
    count=0
    for i in range (length):
        if y[i]!=-1:                
            print (f'{y[i]} \t\t\t {x[i]}')
            count=count+1
    a=[1]*count
    b=[1]*count
    k=0
    for i in range (30):           
            if y[i]!=-1 :
                a[k]=y[i]
                b[k]=x[i]
                k = k + 1
    print (a)
    print (b)
        
        
        
    
main()
