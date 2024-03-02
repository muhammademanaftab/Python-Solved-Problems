def main():
    r=int(input('Enter no of rows: '))
    i=1
    sum=0
    a=1
    j=1
    b=4
    while i<=r:
        while j<=b+1:
            print (a, end=' ')
            sum=sum+a
            a=a+1
            j=j+1
        print ('=',sum)
        a=1
        b=b+1
        sum=0
        j=1
        i=i+1
main()
        
        
