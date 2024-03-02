
from random import *
def main():
    #take input, here I am writing code to take capital character or small character at random
    choice = randint(1, 2)
    if choice == 1: n = randint(65, 90);    #capital letter
    else:           n = randint(97, 122);   #small letter
    print (f'Character: {chr(n)}')
    if n & 1==0:    n = n | 1;
    else:           n = n & ~ 1;
    if n & 2==0:    n = n | 2;
    else:           n = n & ~ 2 ;
    if n & 4==0:    n = n | 4;
    else:           n = n & ~ 4;
    if n & 8==0:    n = n | 8;
    else:           n = n & ~ 8 ;
    if n & 16==0:    n = n | 16;
    else:           n = n & ~ 16 ;
    if n & 32==0:    n = n | 32;
    else:           n = n & ~ 32;
    print (f'Character after flip: {chr(n)}')


main()
