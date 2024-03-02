from random import *
def main():
    r=int(input ('Enter Number of rows: '))
    c=int(input ('Enter Number of columns: '))
    i=1
    j=1
    while i<=r:
        while j<=c:
            x=randint(1,9)
            y=randint(1,9)
            z=str(x)+str(y)
            print (z, end = ' ')
            j=j+1
        print()
        j=1
        i=i+1
main()
