from random import *
x1=randint(0,1000)
x2=randint(0,1000)
x3=randint(0,1000)
x4=randint(0,1000)
print ('Number Before Condtion:  ',x1,x2,x3,x4)

if x1<x2 and x1<x3 and x1<x4 and x2<x3 and x2<x4 and x3<x4:
    x1,x2,x3,x4=x1,x2,x3,x4
if x1<x2 and x1<x3 and x1<x4 and x2<x3 and x2<x4 and x4<x2:
    x1,x2,x3,x4=x1,x2,x4,x3    
if x1<x2 and x1<x3 and x1<x4 and x3<x2 and x3<x4 and x2<x4:
    x1,x2,x3,x4=x1,x3,x2,x4
if x1<x2 and x1<x3 and x1<x4 and x3<x2 and x3<x4 and x4<x2:
    x1,x2,x3,x4=x1,x3,x4,x2
if x1<x2 and x1<x3 and x1<x4 and x4<x2 and x4<x3 and x3<x2:
    x1,x2,x3,x4=x1,x4,x3,x2
if x1<x2 and x1<x3 and x1<x4 and x4<x2 and x4<x3 and x2<x3:
    x1,x2,x3,x4=x1,x4,x2,x3


if x2<x1 and x2<x3 and x2<x4 and x1<x3 and x1<x4 and x3<x4:
    x1,x2,x3,x4=x2,x1,x3,x4
if x2<x1 and x2<x3 and x2<x4 and x1<x3 and x1<x4 and x4<x1:
    x1,x2,x3,x4=x2,x1,x4,x3    
if x2<x1 and x2<x3 and x2<x4 and x3<x1 and x3<x4 and x1<x4:
    x1,x2,x3,x4=x2,x3,x1,x4
if x2<x1 and x2<x3 and x2<x4 and x3<x1 and x3<x4 and x4<x1:
    x1,x2,x3,x4=x2,x3,x4,x1
if x2<x1 and x2<x3 and x2<x4 and x4<x1 and x4<x3 and x3<x1:
    x1,x2,x3,x4=x2,x4,x3,x1
if x2<x1 and x2<x3 and x2<x4 and x4<x1 and x4<x3 and x1<x3:
    x1,x2,x3,x4=x2,x4,x1,x3    
    

if x3<x2 and x3<x1 and x3<x4 and x2<x1 and x2<x4 and x1<x4:
    x1,x2,x3,x4=x3,x2,x3,x4
if x3<x2 and x3<x1 and x3<x4 and x2<x1 and x2<x4 and x4<x1:
    x1,x2,x3,x4=x3,x2,x4,x1    
if x3<x2 and x3<x1 and x3<x4 and x1<x2 and x1<x4 and x2<x4:
    x1,x2,x3,x4=x3,x1,x2,x4
if x3<x2 and x3<x1 and x3<x4 and x1<x2 and x1<x4 and x4<x2:
    x1,x2,x3,x4=x3,x1,x4,x2
if x3<x2 and x3<x1 and x3<x4 and x4<x2 and x4<x1 and x1<x2:
    x1,x2,x3,x4=x3,x4,x1,x2
if x3<x2 and x3<x1 and x3<x4 and x4<x2 and x4<x1 and x2<x1:
    x1,x2,x3,x4=x3,x4,x2,x1

if x4<x2 and x4<x3 and x4<x1 and x2<x3 and x2<x1 and x3<x1:
    x1,x2,x3,x4=x4,x2,x3,x1
if x4<x2 and x4<x3 and x1<x1 and x2<x3 and x2<x1 and x1<x3:
    x1,x2,x3,x4=x3,x2,x1,x3    
if x4<x2 and x4<x3 and x4<x1 and x3<x2 and x3<x1 and x2<x1:
    x1,x2,x3,x4=x4,x3,x2,x1
if x4<x2 and x4<x3 and x4<x1 and x3<x2 and x3<x1 and x1<x2:
    x1,x2,x3,x4=x4,x3,x1,x2
if x4<x2 and x4<x3 and x4<x1 and x1<x2 and x1<x3 and x3<x2:
    x1,x2,x3,x4=x4,x1,x3,x2
if x4<x2 and x4<x3 and x4<x1 and x1<x2 and x1<x3 and x2<x3:
    x1,x2,x3,x4=x4,x1,x2,x3    

print('Number After Condition:  ',x1,x2,x3,x4)

    
    
    
