from random import *
def main():
    x=str(input ('Character:  '))
    y=ord(x)
    a=y^63
    b=chr(a)
    print ('Character After Flip:  ', b)

main()
main()

    
