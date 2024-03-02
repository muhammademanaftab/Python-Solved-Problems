def main():
    n =int(input('N:  '))
    for i in range (1,n+1):
        for j in range (n-i,0,-1):
            print(' ',end='')
        m=i
        for k in range (1,i):
            print (m,end='')
            m=m-1
        print ('1',end='')
        p=1
        for m in range (1,i):
            p=p+1
            print (p,end='')
        
        print()
main()
            
