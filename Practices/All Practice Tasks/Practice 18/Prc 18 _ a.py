def main():
    n=int(input('n:  '))
    i=1 ; k=1
    while i<=n:
        j=1
        k=1
        while k<=i:
            print (k,end='')
            j=1
            while j<i:
                print (' ',end='')
                j=j+1
            k=k+1        
        print()
        i=i+1
main()
            
            
        
