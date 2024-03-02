def main():
    n=int(input('N:  '))
    a=65
    for i in range (1,n+1):        
        for j in range (1,n+1):
            print (chr(a),end=' ')
            a=a+1
            b=1
            for k in range (j):
                print(b,end=' ')
                b=b+1
        print()
main()
                
