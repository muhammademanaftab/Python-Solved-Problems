from random import *

def main():
    n = randint(101, 999)
    print ('Number: ', n)
    print ('First Digit: ', n // 100)
    n = n % 100                                 #To get remaining two digits of n
    print ('Second  Digit: ', n  // 10)
    print ('Third Digit: ', n % 10)

main()