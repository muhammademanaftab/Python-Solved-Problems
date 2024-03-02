def main():
    f1=open ('counts.txt','r')
    i=1
    x=0
    while i<=10000:
        n=int(f1.readline().strip('\n'))
        x=x+n
        i=i+1    
    if x==10000:
        print ('Counts are equal to =',x)
        
main()            
