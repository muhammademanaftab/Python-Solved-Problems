from random import *
x1=randint (1,10)
x=int(input('First Chance:  '))
y=int(input('Second Chance:  '))
z=int(input('Third Chance:  '))
if x==x1 or y==x1 or z==x1:
      print('Winner')
else:
    print('Looser')
    print ('Number:  ',x1)
