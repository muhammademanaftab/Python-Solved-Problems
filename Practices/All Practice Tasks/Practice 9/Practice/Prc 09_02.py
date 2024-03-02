import random
x=random.randint(1,13)
y=random.randrange(0,4)
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

if y==0:
    a='Spade'
elif y==1:
    a='Heart'
elif y==2:
    a='Diamond'
else:
    a='Club'

if x==1 and y==0 or y==1 or y==2 or y==3 :
    print (f'{z} of {a}')
elif x==11 and y==0 or y==1 or y==2 or y==3 :
    print (f'{z} of {a}')
elif x==12 and y==0 or y==1 or y==2 or y==3 :
    print (f'{z} of {a}')
elif x==13 and y==0 or y==1 or y==2 or y==3 :
    print (f'{z} of {a}')
else:
    print (f'{z} of {a}')
    
    
     
    
