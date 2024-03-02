def main():
    x=int(input('Enter number of rows:  '))
    i=1
    a=65
    j=1
    while i<=x:
        while j<=26:
            print(chr(a),end='')
            a=a+1
            j=j+1
        j=1
        a=65
        print()
        i=i+1
main()
        
