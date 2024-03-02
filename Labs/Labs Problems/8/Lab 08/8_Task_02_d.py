def main():
    r=int(input('Enter no of rows:  '))
    c=int(input('Enter no of rows:  '))
    i=1
    j=1
    while i<=r:
        while j<=c:
            print('*',end='')
            j=j+1
        print ('>')
        
        j=1
        i=i+1
main()
