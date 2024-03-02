def main():
    r=int(input('Enter No of rows:  '))
    c=int(input('Enter no of columns:  '))
    i=1
    j=1
    while i<=r:
        while j<=c:
            print('*', end=' ')
            j=j+1
        j=1
        print()
        i=i+1
main()
