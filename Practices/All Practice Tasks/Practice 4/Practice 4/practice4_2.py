from random import *
def main():
    number_to_guess = randint(1, 10)
    guessed_number = int( input ('Guess number in range 1 - 10: ') )
    if guessed_number == number_to_guess:
        print ('You are winner')
        return
    guessed_number = int( input ('Try again to guess number in range 1 - 10: ') )
    if guessed_number == number_to_guess:
        print ('You are winner')
        return
    guessed_number = int( input ('Last chance to to guess number in range 1 - 10: ') )
    if guessed_number == number_to_guess:
        print ('You are winner')
    else:
        print (f'Sorry you are looser, the number is: {number_to_guess}')

main()
