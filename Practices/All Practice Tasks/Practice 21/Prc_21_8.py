def main():
    r=int(input('Rows:  '))
    c=int(input('Columns:  '))
    
    for i in range (c):
        print('o',end='')
    if r==c:
        s=s-1
        for j in range (s):
            print(' ',end='')
    elif r%2==0 :
        for j in range (s):
            print(' ',end='')    
    else:
        s=s-2
        for j in range (s):
            print(' ',end='')            
    for k in range (c):
        print ('o',end='')
    print()
    
    for l in range (r):
        for m in range (c+l,0,-1):
            print(' ',end='')
        print ('o',end='')
        i=1
        s=s-2
        while i<=s:            
            print(' ',end='')
            i=i+1
        if l==r-1:
            print('')
        else:                
            print('o')
    
        
                
            
    
        
main()
