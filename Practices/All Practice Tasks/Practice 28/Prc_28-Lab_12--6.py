from random import *
def main():
    x = [0]*10
    print('List: ', end='')
    for i in range(len(x)):
        x[i] = randint(1, 15)
        print(x[i], end=' ')
    print()
    print()
    print('Elements Not in List: ', end='')
    y = []
    i = 1
    while i <= 15:
        j = 0
        count = 0
        while j <= len(x)-1:
            if i != x[j]:
                count = count+1
            j = j+1
        if count == 10:
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
main()
