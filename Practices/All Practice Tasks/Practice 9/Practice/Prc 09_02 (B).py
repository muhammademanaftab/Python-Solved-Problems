import random

x=random.randint(1,13)
w=random.randint(1,13)
y=random.randrange(0,4)
v=random.randrange(0,4)
f=random.randint(0,1)
g=random.randint(0,1)

if x==1:
    z='Ace'
elif x==11:
    z='Jack'
elif x==12:
    z='Queen'
elif x==13:
    z='King'
else:
    z=str (x)

if f==0:
    j='Red'
else:
    j='Black'

if g==0:
    h='Red'
else:
    h='Black'

if w==1:
    b='Ace'
elif w==11:
    b='Jack'
elif w==12:
    b='Queen'
elif w==13:
    b='King'
else:
    b=str (x)    
    

if y==0:
    a='Spade'
elif y==1:
    a='Heart'
elif y==2:
    a='Diamond'
else:
    a='Club'
    
if v==0:
    c='Spade'
elif v==1:
    c='Heart'
elif v==2:
    c='Diamond'
else:
    c='Club'
    
if z==b:
    print ('Both cards have Same Number')
else:
    print('Both cards have Different Number')
if a==c:
    print('Both cards have same type')
else:
    print ('Both cards have Different Type')
if j==h:
    print ('Both have same color')
else:
    print ('Both have different color')

print (f'{z}\t{b}\t{a}\t{c}\t{j}\t{h}')

    
    
