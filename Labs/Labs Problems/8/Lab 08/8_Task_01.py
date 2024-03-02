def main():
    f1=open('Runs.txt','r')
    n=int(f1.readline())
    i=1
    j=1
    max=0
    average=0
    sum=0
    print ('Number of players:',n)
    while i<=n:
        m=int(f1.readline())        
        print (f'Player {i}:',end=' ')
        while j<=m:
            score=int(f1.readline())
            sum=sum+score
            h=score
            print(h, end=' ')
            if score>max:
                max=score
            j=j+1
            average=sum//m
            
        j=1
        print ('   ',end='')              
        print ('Average:  ', average, end ='   ')
        print ('Max:  ',max)
        sum=0
        h=0
        average=0
        max=0  
        i=i+1
    f1.close()
main()
