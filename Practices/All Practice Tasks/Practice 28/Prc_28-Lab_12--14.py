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
    print('Principal Diagnol Elements:')
    
    for i in range (r):
        for j in range (c):
            if x[i]==x[j]:
                print (x[i][j],end='  ')
            else:
                print (' ',end='  ')
        print()
main()