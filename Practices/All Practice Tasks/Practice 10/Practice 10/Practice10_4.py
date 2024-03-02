from random import *

def main():
    n = 1
    max = -1      #assuming positive numbers for x
    while n <= 5:
        x = randint(1, 900)
        print ('Number: ', x)
        if max < x:
            max = x
        n = n + 1
    print ('Max Number: ', max)

main()
