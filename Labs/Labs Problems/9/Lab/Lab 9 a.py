def main():
    r=int(input('Rows:  '))
    i=1; A=65
    while i<=r:
        j=1
        while j<=r:
            a=1            
            print (chr(A), end=' ')
            while a<=j:
                print (a, end=' ')
                a=a+1
            A=A+1
            j=j+1
        print()
        i=i+1
main()
        
