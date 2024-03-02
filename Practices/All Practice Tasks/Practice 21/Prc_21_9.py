def main():
    r=int(input('Rows:  '))
    m=r*2
    for i in range (1,r+1):
        for j in range (1,i):
            print ('o',end='')
        k=1
        while k<=m:
            print('*',end='')
            k=k+1
        m=m-2
        for n in range (1,i):
            print ('o',end='')
        print()
    s=2
    for o in range (1,r+1):
        p=1
        while p<=r-o:
            print ('o',end='')
            p=p+1
        q=1
        while q<=s:
            print ('*',end='')
            q=q+1
        s=s+2
        t=1
        while t<=r-o:
            print ('o',end='')
            t=t+1
        print ()
            
            
main()            
        
