def main():
    x=int(input())
    r=''
    while x!=0:
        y=x%8
        x=x//8
        r=str(y)+r
    print (r)
main()
