from random import *
def main ():
    x=[0]*5
    y=[0]*5
    print('List 1: ',end='')
    for i in range (len(x)):
        x[i]=randint(1,9)
        print(x[i],end=' ')
    print()
    print('List 2: ',end='')
    for i in range (len(y)):
        y[i]=randint(1,9)
        print(y[i],end=' ')
    print()
    print()
    print('In Ascending Order: ')
    for j in range (len(x)-1):
        for i in range (len(x)-1):
            if x[i]>x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
    for i in range (len(x)):
        print(x[i],end=' ')
    print()
    for j in range (len(y)-1):
        for i in range (len(y)-1):
            if y[i]>y[i+1]:
                y[i],y[i+1]=y[i+1],y[i]
    for i in range (len(y)):
        print(y[i],end=' ')
    print()
    print()
    print('Together in One List: ',end='')
    z=[]
    for i in range (len(x)):
        z.append(x[i])    
    for i in range (len(y)):
        z.append(y[i])    
    for i in range (len(z)):
        print (z[i],end=' ')
main()