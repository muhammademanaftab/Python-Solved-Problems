from random import *

def main():
    n = 1
    sum = 0
    while n <= 5:
        x = randint(1, 9)
        print ('Number: ', x)
        sum = sum + x
        n = n + 1
    print ('Sum: ', sum)

main()
