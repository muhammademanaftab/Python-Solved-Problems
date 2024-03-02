from random import *

def main():
    type1 = randint(0, 3)    #there are four types 0, 1, 2 & 3
    if type1 == 0:   type1 = 'D'; clr1 = 'R';
    elif type1 == 1: type1 = 'H'; clr1 = 'R';
    elif type1 == 2: type1 = 'S'; clr1 = 'B';
    else:            type1 = 'C'; clr1 = 'B';
    n1 = randint(1, 13)      #card number 1 to three
    print (f'Card 1 has value {n1} and type is {type1}')

    type2 = randint(0, 3)    #there are four types 0, 1, 2 & 3
    if type2 == 0:   type2 = 'D'; clr2 = 'R';
    elif type2 == 1: type2 = 'H'; clr2 = 'R';
    elif type2 == 2: type2 = 'S'; clr2 = 'B';
    else: type2 = 'C'; clr2 = 'B';
    n2 = randint(1, 13)      #card number 1 to three
    print (f'Card 2 has value {n2} and type is {type2}')

    if n1 == n2:            print ('Both cards have same number');
    elif type1 == type2:    print ('Both cards have same type');
    elif clr1 == clr2:    print ('Both cards have same color');
    elif n1 == n2 + 1 or n1 + 1 == n2:  print ('Both cards are in sequence')

main()