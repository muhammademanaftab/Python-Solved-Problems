from random import *

def main():
    n = randint(101, 999)
    print ('Number: ', n)
    reverse_number = n % 10                     #To get third digit of n
    first_digit = n // 100
    n = n % 100                                 #To get remaining two digits of n
    second_digit = n // 10
    reverse_number = reverse_number * 100 + second_digit * 10 + first_digit
    print ('Reverse Number: ', reverse_number)

main()