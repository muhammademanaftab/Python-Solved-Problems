def main():
    r=int(input('Rows:  '))
    for i in range (1,r):
        a=65
        for j in range (26):
            print (chr(a),end='')
            a=a+1
        print()
            
main()
