def main():
    n=int(input('N:  '))
    i=1
    a=(n*2)-2
    k=1
    
    while i<=n:        
        j=1
        while j<i:           
           print (' ',end='')
           j=j+1
        print ('*',end='')
        j=1
        while j<a:
            print (' ',end='')
            j=j+1
        if i<n:
            print ('*',end='')
        j=1
        while  j<k:
            print (' ',end='')            
            j=j+1
                
        if i!=k:
            print('*',end='')
        j=1
        while j<a:
            print(' ',end='')
            j=j+1
        if i==k:
            print(' ',end='')
        if i<n:
            print('*')
        
        a=a-2
        k=k+2
        i=i+1
        
        
        
main()
