def main():
    r=int(input ('Enter Number of rows:  '))
    i=1
    j=1
    a=1
    while i<=r:
        while j<=5:
            print (a, end=' ')
            a=a+1
            j=j+1
        j=1
        print()
        i=i+1
        a=i
main()
