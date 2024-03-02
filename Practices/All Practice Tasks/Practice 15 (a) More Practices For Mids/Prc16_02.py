from random import *
i=1
count0=0
count1=0
while i<=5:
    x=randint(0,1)
    print(x)
    if x==0:
        count0=count0+1
    
    if x==1:
        count1=count1+1

    i=i+1
print ('Count of 0:  ', count0)
print ('Count of 1:  ',count1)
        
