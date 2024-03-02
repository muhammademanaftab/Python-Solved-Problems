from random import *
def main():
    i=0
    while i<=5:
        x=randint (65,90)
        y=chr(x)
        if y!='A' or y!='E' or y!='I' or y!='O' or y!='U':
            i=i+1
            print (y, end='  ')

main()
