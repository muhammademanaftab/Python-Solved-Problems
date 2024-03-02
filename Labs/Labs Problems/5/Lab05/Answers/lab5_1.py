from random import *

def main():
    n = randint(20, 99)
    f = n // 10     # first digit of n
    s = n % 10      # second digit of n
    print (f'Number {n} in English is ', end='')
    if f==2:    print ('twenty', end='');
    elif f==3:    print ('thirty', end='');
    elif f==4:    print ('fourty', end='');
    elif f==5:    print ('fifty', end='');
    elif f==6:    print ('sixty', end='');
    elif f==7:    print ('seventy', end='');
    elif f==8:    print ('eighty', end='');
    else:    print ('ninety', end='');

    if s==1:    print ('-one');
    elif s==2:    print ('-two');
    elif s==3:    print ('-three');
    elif s==4:    print ('-four');
    elif s==5:    print ('-five');
    elif s==6:    print ('-six');
    elif s==7:    print ('-seven');
    elif s==8:    print ('-eight');
    elif s==9:    print ('-nine');

main()
