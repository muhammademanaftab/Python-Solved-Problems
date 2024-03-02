def main():
    r=int(input('Rows:  '))
    c=int(input('Columns:  '))
    for i in range  (c):
        print ('o',end='')
    for j in range (r):
        print (' ',end='')
    for k in range (c):
        print ('o',end='')
    print()
    k=0
    for m in range (r//2):
        i=0
        while i<c+m:
            print(' ',end='')
            i=i+1
        print ('o',end='')
        j=1       
        while j<=r-k-2:
            print(' ',end='')
            j=j+1
        k=k+2
        print('o')
    q=1
    if c%2==0:
        for n in range (c+(c//2)-1):
            print (' ',end='')
    else:
        for n in range (c+(c//2)):
            print (' ',end='')
    print ('o')
    for o in range ((r//2)):
        p=0
        if c%2==0:                
            while p<=c+1-o:
                print (' ',end='')
                p=p+1
        else:                
            while p<=c-o:
                print (' ',end='')
                p=p+1
        print ('o',end='')
        r=1
        while r<=q:
            print (' ',end='')
            r=r+1
        q=q+2
        print ('o')
    for s in range (c):
        print('o',end='')
    for t in range (r):
        print (' ',end='')
    for u in range (c):
        print ('o',end='')
    print()
        
        
main()
        

    
        
        
