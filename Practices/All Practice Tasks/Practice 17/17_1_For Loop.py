def main():
    n=int(input('N:  '))
    k=int(input('K:  '))
    for i in range (1,n+1):
        a=1
        for j in range (k):
            print (i,end='     ')
            print (a)
            a=a+1
main()
