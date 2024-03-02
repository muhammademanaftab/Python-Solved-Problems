def main():
    f1 = open('nums.txt', 'r')
    i=1
    x=0
    while i<=10000:        
        n=int(f1.readline())
        x=x+n
        i=i+1
    x=x/i
    print ('Average:  ',x)
main()
    
