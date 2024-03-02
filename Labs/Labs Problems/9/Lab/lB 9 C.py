def main():
    n=int(input('Enter Rows:  '))
    i=1
    k=(n*4)-4
    while i<=n:
        j=1
        while j<i:
            print ('  ',end='')
            j=j+1
        print ('|',end='')
        print ('_',end='')
        j=1
        while j<k:
            print (' ',end='')
            j=j+1
        
        if i<n:
            print ('_',end='')
        
        print('|')        
        k=k-4
        i=i+1
main()
