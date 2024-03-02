def main ():
    x=str(input('Enter First Character:  '))
    y=str(input ('Enter Second Character:  '))
    a=ord(x)
    b=ord(y)
    c=a^b
    if c==0:
        print (f'\'{x}\' and \'{y}\' are same')
    else:
        print (f'\'{x}\' and \'{y}\' are different')

main()
main()
    
