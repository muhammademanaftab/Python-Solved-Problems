from random import *
def main():
    a=randint (1,13)
    b=randint (1,13)
    c=randint (1,13)
    d=randint (0,3)
    e=randint (0,3)
    f=randint (0,3)
    g=randint (0,1)
    h=randint (0,1)
    i=randint (0,1)

    if a==1:
        j='Ace'
    elif a==11:
        j='Jack'
    elif a==12:
        j='Queen'
    elif a==13:
        j='King'
    else:
        j=str(a)

    if d==0:
        k='Diamond'
    if d==1:
        k='Heart'
    if d==2:
        k='Spade'
    if d==3:
        k='Club'

    if g==1:
        l='Red'
    else:
        l='Black'


        # Second Card


    if b==1:
        m='Ace'
    elif b==11:
        m='Jack'
    elif b==12:
        m='Queen'
    elif b==13:
        m='King'
    else:
        m=str(a)

    if e==0:
        n='Diamond'
    if e==1:
        n='Heart'
    if e==2:
        n='Spade'
    if e==3:
        n='Club'

    if h==1:
        o='Red'
    else:
        o='Black'

        #3rd Card

    if c==1:
        p='Ace'
    elif c==11:
        p='Jack'
    elif c==12:
        p='Queen'
    elif c==13:
        p='King'
    else:
        p=str(a)

    if f==0:
        q='Diamond'
    if f==1:
        q='Heart'
    if f==2:
        q='Spade'
    if f==3:
        q='Club'

    if i==1:
        r='Red'
    else:
        r='Black'

    if j==m and j==p and m==p and k==n and k==q and n==k :
        print ('All cards have same number and of same type')
    if k==n and k==q and n==q:
        print ('All cards have same type')
    if l==o and l==r and o==r:
        print ('All cards have same number')
    if j==m and j==p:
        print('Two cards have same type')
    if m==p and m==j:
        print ('Two cards have same type')

    else :
        print (f'
        

        
        

        



        
        

        
        
        
        

    
