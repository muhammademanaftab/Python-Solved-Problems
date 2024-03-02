def main():
    n=int(input('N:  '))
    for i in range (n):
        for k in range (i):
            print (' ',end='')
        for j in range (n-i,0,-1):
            print ('+',end='')
        print()
    
    for a in range (1,n):
        for l in range (n-a,1,-1):
            print(' ',end='')
        for m in range (0,a+1):
            print('+',end='')
        print()
main()
