def main():
    r=int(input('Rows:  '))
    for i in range (1,r+1):
        a=1
        sum=0
        for j in range (1,5+i):
            print(a,end=' ')
            sum= sum+a
            a=a+1
        print ('=',sum)
main()
            
