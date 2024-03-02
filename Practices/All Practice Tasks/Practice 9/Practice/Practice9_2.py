from random import *

def main():
    card_number = randint(1, 13)
    card_type = randint(0, 3)    #there are four types 0, 1, 2 & 3
    if card_number == 1:    print ('Ace of ', end = '');
    elif card_number == 2:  print ('Two of ', end = '');
    elif card_number == 3:  print ('Three of ', end = '');
    elif card_number == 4:  print ('Four of ', end = '');
    elif card_number == 5:  print ('Five of ', end = '');
    elif card_number == 6:  print ('Six of ', end = '');
    elif card_number == 7:  print ('Seven of ', end = '');
    elif card_number == 8:  print ('Eight of ', end = '');
    elif card_number == 9:  print ('Nine of ', end = '');
    elif card_number == 10:  print ('Ten of ', end = '');
    elif card_number == 11:  print ('Jack of ', end = '');
    elif card_number == 12:  print ('Queen of ', end = '');
    else:                     print ('Kind of ', end = '');
    if card_type == 0:      print ('Diamond');
    elif card_type == 1:    print ('Heart');
    elif card_type == 2:    print ('Spade');
    else: card_type = 3;    print ('Club')

main()