def main():
    f1=open('Runs.txt','r')
    n=int(f1.readline())
    i=1
    j=1
    max=0
    average=0
    sum=0
    while i<=n:
        m=int(f1.readline())
        print ('Number of players:  ',n, end=' ')        
        while j<=m:
            score=int(f1.readline())
            sum=sum+score
            m=score
            print ('Player 1:  ',)
            if score>max:
                max=score
            average=sum//m
            print ('Average:  ', average)
            print ('Max:  ',max)
main()
            
