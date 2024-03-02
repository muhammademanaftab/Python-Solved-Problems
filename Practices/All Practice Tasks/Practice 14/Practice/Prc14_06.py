def main():
    i=1
    b=1
    a=1
    while i<=26:
        a=i+64
        A=chr(a)
        if A=='A' or A=='E' or A=='I' or A=='O' or A=='U':
            print()
            print (A)
            
        
        else:
            print (A , end=' ')
        i=i+1
main()
