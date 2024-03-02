from random import *
x=randint(1,10)
y=int(input('Guess The Number:  '))
if y==x:
    print ('Winner')
    
else:
    z=int(input('Guess The Number:  '))
    if z==x:
        print('Winner')
    else:
         a=int(input('Guess The Number:  '))
         if a==z:
             print ('Winner')
         else:
              print ('Looser')
              print ('The Number is :  ',x)

              
    
