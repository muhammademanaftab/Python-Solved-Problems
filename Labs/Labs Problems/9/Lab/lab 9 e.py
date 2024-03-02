def main():
    r=int(input('Rows:  '))
    c=int(input('Columns:  ')) 
    i=1
    while i<=r:
        j=1
        k=1
        sum=0
        while j<=c:
            print (k,end='')
            sum=sum+k
            if j==c:
                print('',end='')
            else:
                print('+',end='')
            k=k+i
            j=j+1
        print ('=',end='')
        print(sum)
        i=i+1
       
main()
