def main():
    n=int(input('N:  '))
    m=int(input('K:  '))
    for i in range (1,n+1):
        print('{',end='')
        for j in range (1,m+1):
            print ('(',i,',',j,')',end='')
            if i<m and j<n:
                print (',',end='')
        print('}',end='')
main()
            
