def main():
    n=int(input('N:  '))
    for i in range (1,n+1):
        a=97
        for j in range (6):
            print(chr(a),end=' ')
            a=a+i
        print()
main()
