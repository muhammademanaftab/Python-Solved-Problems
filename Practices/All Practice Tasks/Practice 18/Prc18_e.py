def main():
    n=int(input('N:  '))
    i=1
    while i<n:
        j=1
        a=97
        while j<=6:
            print (chr(a),end=' ')
            a=a+i
            j=j+1
        print()
        i=i+1
        
main()
