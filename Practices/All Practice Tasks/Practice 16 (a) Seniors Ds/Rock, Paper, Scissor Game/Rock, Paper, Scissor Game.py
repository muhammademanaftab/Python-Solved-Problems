from random import *
def main():
    a=input('Wanna Play Game Y/N:  ')
    while a=='Y' or a=='y' or a=='yes':
        x=randint(1,3)
        if x==1:
            y='Rock' or y=='rock'
        if x==2:
            y='Paper' or y=='paper'
        if x==3:
            y='Scissor' or y=='scissor'
        b=str(input('Enter your choice:  ', ))
        print ('Computers Choice is :  ',y)
        if y=='Rock'and (b=='Scissor' or b=='scissor') :
            print ('Rock Smashes the Scissor')
            print ('You Looser, Computer is Winner')
        elif y=='Scissor' and (b=='Rock' or b=='rock'):
            print ('Rock Smashes the Scissor')
            print ('Congratualtions, you are winner')
        elif y=='Scissor' and (b=='Paper' or b=='paper'):
            print ('Scissor cuts the paper')
            print ('You Looser,Computer is Winner')
        elif y=='Paper' and (b=='Scissor' or b=='scissor'):
            print ('Scissor cuts the paper')
            print('Congratulations, you are winner')
        elif y=='Rock' and (b=='Paper' or b=='paper'):
            print ('Congratulations, you are winner')
        elif y=='Paper' and (b=='Rock' or b=='rock'):
            print ('You Looser, Computer is winner')
        else:
            print ('Game is Drawn')
        a=str(input('Wanna Play Again Y/N:  '))
main()
        
        
