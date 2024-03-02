from random import *
def main():
    r=10
    c=10
    x=[[randint(0,9) for j in range (c)] for i in range (r)]
    print('Matrix: ')    
    for i in range (r):
        for j in range (c):
            print (x[i][j],end='  ')
        print()
    print()
    print ('After Replacing Zeros:')
    for i in range (r):
        for j in range (c):
            if x[i][j]==0:
                x[i][j]=1
    for i in range (r):
        for j in range (c):
            print (x[i][j],end='  ')
        print()
    print()
main()