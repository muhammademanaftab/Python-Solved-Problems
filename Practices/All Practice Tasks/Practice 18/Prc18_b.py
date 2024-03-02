def main():
    n=int(input('N:  '))
    i=1
    while i<=n:
        j=1
        while j<=i:
            print ('+',end='')
            j=j+1
        print()
        i=i+1
    j=1
    i=i-1
    while i>j:
        while j<i:
            print ('+',end='')
            j=j+1
        print('')
        j=1
        i=i-1        
main()
