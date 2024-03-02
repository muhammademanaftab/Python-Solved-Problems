def main():
    n = 1
    while n <= 100:
        f = n // 10     # first digit of n
        s = n % 10      # second digit of n
        if f==2:      print ('twenty', end=' ');
        elif f==3:    print ('thirty', end=' ');
        elif f==4:    print ('fourty', end=' ');
        elif f==5:    print ('fifty', end=' ');
        elif f==6:    print ('sixty', end=' ');
        elif f==7:    print ('seventy', end=' ');
        elif f==8:    print ('eighty', end=' ');
        elif f==9:    print ('ninety', end=' ');

        if n == 10:     print ('ten', end='');
        elif n == 11:   print ('eleven');
        elif n == 12:   print ('twelve');
        elif n == 13:   print ('thirteen');
        elif n == 14:   print ('fourteen');
        elif n == 15:   print ('fifteen');
        elif n == 16:   print ('sixteen');
        elif n == 17:   print ('seventeen');
        elif n == 18:   print ('eighteen');
        elif n == 19:   print ('nineteen');
        elif n == 100:   print ('hundred', end='');
        elif s==1:    print ('one');
        elif s==2:    print ('two');
        elif s==3:    print ('three');
        elif s==4:    print ('four');
        elif s==5:    print ('five');
        elif s==6:    print ('six');
        elif s==7:    print ('seven');
        elif s==8:    print ('eight');
        elif s==9:    print ('nine');
        if s==0:      print ();
        n = n + 1

main()
