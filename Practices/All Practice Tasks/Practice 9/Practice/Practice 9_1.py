from random import *

def main():
    card_number = randint(1, 13)
    card_type = randint(0, 3)    #there are four types 0, 1, 2 & 3
    if card_type == 0:   card_type = 'D';
    elif card_type == 1: card_type = 'H';
    elif card_type == 2: card_type = 'S';
    else:                card_type = 'C';
    print ('Card Type is ', card_type)
    if card_type == 'S' or card_type == 'C' : print ('Card Color is Black');
    else:                                       print ('Card Color is Red');

main()