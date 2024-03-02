def main():
    a=65
    n=int(input('Rows:  '))
    for i in range (1,n+1):
        for j in range (4):
            print (chr(a),end=' ')
            a=a+1
        print()
main()
