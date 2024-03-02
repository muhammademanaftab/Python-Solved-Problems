A=int(input('Amount Deposited:  '))

if A<=500000:
    One=0.07*A
    O=One+A
    Two=0.07*O
    T=O+Two
    Three=T*0.07
    Tr=T+Three
    print ('Amount Deposited:  \t\t\t', A)
    print ('Amount after one year:  \t\t', O)
    print ('Amount after two year:  \t\t', T)
    print ('Amount after three year:  \t\t',Tr)

else :
    
    One=0.1*A
    O=One+A
    Two=0.1*O
    T=O+Two
    Three=0.1*T
    Tr=T+Three
    print ('Amount Deposited:  \t\t\t', A)
    print ('Amount after one year:  \t\t', O)
    print ('Amount after two year:  \t\t', T)
    print ('Amount after three year:  \t\t',Tr)


        
