x=int (input ('Enter Amount:  '))
y= (input ('Enter Category:  '))
if x>0 and x<=100:
    if y== 't' or y== 'T':
        t=x        
        d1=0.0*x
    if y=='p' or y== 'P':
        p=0.95*x
        d2=0.5*x
    if y== 's' or y== 'S':
        s=0.90*x        
        d3=0.10*x

elif x>101 and x<200:
    if y== 't' or y== 'T':
        t=0.95*x        
        d1=0.05*x
    if y== 'p' or y=='P':
         p=0.90*x         
         d2=0.10*x
    if y=='s' or y=='S':
         s=0.85*x         
         d3=0.15*x
elif x>201 and x<300:
    if y=='t' or y=='T':
        t=0.90*x        
        d1=0.10*x
    if y=='p' or y=='P':
        p=0.85*x        
        d2=0.15*x
    if y=='s' or y=='S':
        s=0.80*x        
        d3=0.20*x
else:
    if y=='t' or y=='T':
        t=0.85*x        
        d1=0.15*x
    if y=='p' or y=='P':
        p=0.80*x       
        d2=0.20*x
    if y=='s' or y=='S':
        s=0.85*x        
        d3=0.25*x    

    
print ('Output:  ')
print ('Amount:\t\t', x)
print ('Category:  ', y)
if y== 't' or y=='T':
    print('Discount:  ', d1)
elif y=='p' or y=='T':
    print ('Discount:  ',d2)
else:
    print ('Discount:  ',d3)
    
if y=='t' or y=='T':
    print('Bill:  ',t)

elif y=='p' or y== 'P':
    print ('Bill:  ',p)

else:
     print ('Bill:  ',s)
