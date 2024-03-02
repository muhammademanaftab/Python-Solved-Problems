from random import *

def main():
    i = 1
    sum_even = sum_odd = 0
    while i <= 10:
        number = randint(1, 100)
        print (number, end = ' ')
        if number % 2 == 0: sum_even = sum_even + number;
        else:               sum_odd = sum_odd + number;
        i = i + 1
    print ('\nSum of even numbers: ', sum_even)
    print ('Sum of odd numbers: ', sum_odd)


main()
