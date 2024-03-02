def main():
    r=int(input('Rows:  '))
    i=1    
    while i<=r:
        j=i        
        while j<r:
            print(' ',end='')
            j=j+1
        m=2
        j=i
        while j>=m:           
            print (j, end='')
            j=j-1            
        k=1
        print(k,end='')               
        while k<i:
            print (k+1,end='')
            k=k+1
        print()
        i=i+1
main()
