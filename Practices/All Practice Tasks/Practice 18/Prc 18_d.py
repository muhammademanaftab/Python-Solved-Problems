def main():
    n=int(input('N:  '))
    i=1
    while i<=n:
        k=0
        k=k+i
        while k<=n:
            print ('+',end='')
            k=k+1
        k=1
        while k<i:
            print(' ',end='')
            k=k+1
            
        k=1        
        while i>k:
            print(' ',end='')
            k=k+1
        k=0
        j=n-i
        while j>=k:
            print('+',end='')
            j=j-1
        print()
        i=i+1  
    i=1
    while i<n:
        k=0
        while k<=i:
            print('+',end='')
            k=k+1
        k=i+1
        j=n
        while k<n:
            print(' ',end='')
            k=k+1
            
        j=n-i
        k=1
        while k<j:
            print(' ',end='')
            k=k+1
        m=0
        while m<=i:
            print('+',end='')
            m=m+1
        print()
        i=i+1
    
main()
