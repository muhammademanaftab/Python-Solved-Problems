def main():
    r = int(input('R:  '))
    for i in range (r):
        for j in range (2*i):
            print(' ',end='')
        print ('|',end='')
        print ('_',end='')
        for k in range (1,((r*4)-4)-(i*4)):
            print(' ',end='')
        if i==r-1: print('',end='')
        else: print ('_',end='')
        print ('|')
        
main()
        
