from random import *
def main():
    x=[1]*12
    for i in range (12):
        x[i]=randint (1000,2000)
        print (x[i],end='  ')
    print()
    first_six=0
    second_six=0
    for i in range (5):
        first_six=first_six+x[i]
        second_six=second_six+(x[i+6])
    print ('First Half:',first_six)
    print ('Second Half:',second_six)
    print()
    print ('Quarter Wise')
    first_quarter=0
    second_quarter=0
    third_quarter=0
    fourth_quarter=0
    for i in range (3):
        first_quarter=first_quarter+x[i]
        second_quarter=second_quarter+x[i+3]
        third_quarter=third_quarter+x[i+6]
        fourth_quarter=fourth_quarter+x[i+9]
    print ('Sale in First Quarter:',first_quarter)
    print ('Sale in Second Quarter:',second_quarter)
    print ('Sale in Third Quarter:',third_quarter)
    print ('Sale in Fourth Quarter:',fourth_quarter)      
main()
