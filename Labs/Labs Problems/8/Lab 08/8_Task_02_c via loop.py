def main():
    x=int(input('Enter Number:  '))
    i=1
    j=1
    while i<=x:
        while j<=i:
            print ('*',end=' ')
            j=j+1
        print()
        j=1
        i=i+1
main()
