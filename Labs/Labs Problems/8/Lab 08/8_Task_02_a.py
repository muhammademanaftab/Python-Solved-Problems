def main():
    r=int(input('Enter number of rows:  '))
    i=1
    j=1
    a=65
    while i<=r:
        while j<=4:
            print(chr(a), end=' ')
            a=a+1
            j=j+1
        j=1
        print()
        i=i+1
        
main()
