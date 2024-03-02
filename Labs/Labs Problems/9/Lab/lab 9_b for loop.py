def main():
    n=int(input('N:  '))
    for i in range (1,n+1):
        for j in range (2,i+1):
            print (' ',end='')
        print('*',end='')
        for k in range ((n*2)-(i*2),1,-1):
            print (' ',end='')
        if i==n:
            print('',end='')
        else:
            print('*',end='')
        if i==2:
            print (' ',end='')
        else:
            for k in range (3,(i*2)):
                 print (' ',end='')
        if i==1:
            print ('',end='')
        else:
            print('*',end='')
        for k in range ((n*2)-(i*2),1,-1):
            print (' ',end='')
        if i==n:
            print('',end='')
        else:
            print('*',end='')
            
        print()
        
main()
        
