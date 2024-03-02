from random import *
def main():
    x=[0]*20
    for i in range (len(x)):
        x[i]=randint(1,50)
    for j in range (len(x)-1):
        for i in range (len(x)-1):
            if x[i]>x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
    for i in range (len(x)):
        print(x[i],end='  ')
    print()
    print()
    print('Elements Not in List: ', end='')
    y = []
    i = 1
    while i <= 50:
        j = 0
        count = 0
        while j <= len(x)-1:
            if i != x[j]:
                count = count+1
            j = j+1
        if count == 20:
            y.append(i)
        i = i+1  
    for i in range(len(y)):
        print(y[i], end=' ')
    print()
    print()
    print('Modified List: ', end='')
    k = 0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] == x[j]:
                x[j] = y[k]
                k=k+1
    for i in range(len(x)):
        print(x[i], end=' ')
    print()
    print()

    print('After Sorting: ',end='')

    for i in range (len(x)-1):
        for j in range (len(x)-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]


    for i in range(len(x)):
        print(x[i], end=' ')
    print()
    print()           


    
    for i in range (len(x)-1):
        j=x[i]
        k=x[i+1]
        while j<k:
            j=j+1
            if j!=k:
                print(j,end=' ')
main()