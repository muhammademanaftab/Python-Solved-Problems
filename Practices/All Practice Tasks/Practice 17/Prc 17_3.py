def main():
    n=int(input('N:  '))
    k=int(input('K:  '))
    i=1
    print ('{',end='')
    while i<=n:
        j=1
        while j<=k:
            print ('(',i,',',j,')', end=' ')
            j=j+1
            if i<=n and j<=k:
                print (',' ,end =' ')
        
        i=i+1
    print('}')

main()
