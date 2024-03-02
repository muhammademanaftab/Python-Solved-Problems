def main():
    n=int(input('N:  '))
    k=int(input('K:  '))
    i=1 ; a=1 
    while i<=n:
        b=1
        j=1
        while j<=k:
            print (a, end='       ')
            print (b)
            b=b+1
            j=j+1
        a=a+1
        i=i+1
main()
            
    
