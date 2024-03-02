#Task_01
from random import *
x1= randint (1,1000)
x2= randint (1,1000)
x3= randint (1,1000)
x4= randint (1,1000)
#Numbers before condition
print(f'Numbers before condtion: \t{x1}\t{x2}\t{x3}\t{x4}')

#Numbers after condtion
if x1<x2 and x1<x3 and x1<x4:
    x=x1
    if x2<x3 and x2<x4:
        y=x2
        if x3<x4:
            z=x3
            a=x4
        else:
            z=x4
            a=x3
    elif x3<x2 and x3<x4:
        y=x3
        if x2<x4:
            z=x2
            a=x4
        else:
            z=x4
            a=x2
    else:
         y=x4
         if x2<x3:
             z=x2
             a=x3
         else:
             z=x3
             a=x2
elif x2<x1 and x2<x3 and x2< x4:
    x=x2     
    if x1<x3 and x1<x4:
        y=x1
        if x3<x4:
            z=x3
            a=x4
        else:
            z=x4
            a=x3
    elif x3<x1 and x3<x4:
        y=x3
        if x1<x4:
            z=x1
            a=x4
        else:
            z=x1
            a=x4
    else:
         y=x4
         if x1<x3:
             z=x1
             a=x3
         else:
             z=x3
             a=x1
elif x3<x1 and x3<x2 and x3< x4:
    x=x3     
    if x2<x1 and x2<x4:
        y=x2
        if x1<x4:
            z=x1
            a=x4
        else:
            z=x4
            a=x1
    elif x1<x2 and x1<x4:
        y=x1
        if x2<x4:
            z=x2
            a=x4
        else:
            z=x4
            a=x2
    else:
         y=x4
         if x2<x1:
             z=x2
             a=x1
         else:
             z=x3
             a=x1             
else:
    x=x4
    if x2<x3 and x2<x1:
        y=x2
        if x3<x1:
            z=x3
            a=x1
        else:
            z=x1
            a=x3
    elif x3<x2 and x3<x1:
        y=x3
        if x2<x1:
            z=x2
            a=x1
        else:
            z=x1
            a=x2
    else:
         y=x1
         if x2<x3:
             z=x2
             a=x3
         else:
             z=x3
             a=x2

print(f'Numbers after condition: \t{x}\t{y}\t{z}\t{a}')

#Task 02:

from random import *
x1= randint (1,1000)
x2= randint (1,1000)
x3= randint (1,1000)
x4= randint (1,1000)

if x1<x2 and x1<x3 and x1<x4:
    if x2<x3 and x2<x4:
        print ('Numbers are in order')
    else:
        print ('Numbers are out of order')
else:
    print ('Numbers are out of order')
      
        
      
