def main():
    f1=open('Count.txt','r')
    x=int(f1.readline())
    i=1
    b=0
    y=1
    while i<=x:
        f2=open('Stars.txt','w')        
        print ('*',end=' ')
        f2.write ('*')
        b=b+1
        if b==y:
            b=0
            y=y+1
            i=i+1
            print()
    
main()
