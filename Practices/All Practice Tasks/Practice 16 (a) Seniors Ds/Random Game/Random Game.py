from random import *
def main():   
    i=str(input('Wanna Play Game Y/N:  '))
    while i== 'Y' or i=='y':
        y=randint(1,10)
        print(f'Number is :    {y}')
        x=int(input('Guess the Number:  '))
        guesses=0
        if x==y:
            print('Congratulations, you guessed the right number')
            guesses=guesses+1
            print('Number of Guesses:  ',guesses)
        while x!=y:
            if x>y:
                print('Too high, try again')
                guesses=guesses+1
            if x<y:
                print('Too low, try again')
                guesses=guesses+1
            x=int(input('Guess the Number:  '))
            if x==y:
                print('Congratulations, you guessed the right number')
                guesses=guesses+1
                print('Number of Guesses:  ',guesses)                
        i=str(input('Wanna Play Game Y/N:  '))
main()
        
            
            
