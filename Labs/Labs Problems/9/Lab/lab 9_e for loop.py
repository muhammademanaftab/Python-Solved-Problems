def main():
    r=int(input('Rows:  '))
    c=int(input('Columns:  '))
    for i in range (1,r+1):
        k=1
        sum=0
        for j in range (1,c+1):
            print (k,end='')
            if j==c:
                print('',end='')
            else:   print('+',end='')
            
            sum=sum+k
            k=k+i
        print (' =',sum)
main()
