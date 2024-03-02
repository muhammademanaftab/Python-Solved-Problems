def main():
    x=int(input('Enter Number:  '))
    b=0
    y=1
    i=1
    while i<=x:
        print ('*',end=' ')
        b=b+1
        if b==y:
            b=0
            y=y+1
            i=i+1
            print()       
main()
            
