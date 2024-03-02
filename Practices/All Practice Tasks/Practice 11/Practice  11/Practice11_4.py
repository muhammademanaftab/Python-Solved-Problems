from random import *

def main():
    i = 1
    while i <= 10:
        alphabet = chr(randint(65, 90))
        print ('Alphabet: ', alphabet, end = '\t')
        if alphabet == 'A' or alphabet == 'E' or alphabet == 'I' or alphabet == 'O' or alphabet == 'U':
            print ('Wovel')
        else:
            print ('Consonent')
        i = i + 1

main()
