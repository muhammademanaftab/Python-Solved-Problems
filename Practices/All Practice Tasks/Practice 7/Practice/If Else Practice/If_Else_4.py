x= input ('Enter Your Name:  ')
y= input ('Enter Your Booking:  ')
z= input ('Enter Type of Seats:  ')
pe= int (input ('Enter Number of Persons:  '))
g=1500
fc=2500
p=3000
v=4000

if y== 'online' or y== 'Online':
    if z== 'g' or z== 'G' :
        d=0.1*g*pe
        b=0.90*g*pe
        c=g*p
    elif z== 'fc' or z== 'FC':
        b=0.90*fc*pe
        d=0.1*fc*pe
        c=fc*p
    elif z=='p' or z=='P':
        d=0.1*p*pe
        b=0.90*p*pe
        c=p*pe
    elif z=='v' or z== 'V':
        d=0.1*v*pe
        b=0.90*v*pe
        c=pe*v
    else:
        c= str ('Missing Information')
        b= str ('Missing Information')
        d= str ('Missing Information')
else:
    c= str ('Missing Information')
    b= str ('Missing Information')
    d= str ('Missing Information')

if y=='Window' or y=='window':
    if z=='g' or z=='G' :
        d=0.05*g*pe
        b=0.95*g*pe
        c=g*pe
    elif z== 'fc' or z== 'FC':
        d=0.05*fc*pe
        b=0.95*fc*pe
        c=fc*pe
    elif z=='p' or z=='P':
        d=0.05*p*pe
        b=b=0.95*p*pe
        c=pe*p
    elif z=='v' or z=='V':
        d=0.05*v*pe
        b=0.95*v*pe
        c=v*pe
    else :
        c= str ('Missing Information')
        b= str ('Missing Information')
        d= str ('Missing Information')
else:
    c= str ('Missing Information')
    b= str ('Missing Information')
    d= str ('Missing Information')

print ('Name:  \t\t\t',x)
print ('No. Of Seats:  \t\t',pe)
print ('Type of seats:  \t',z)
print ('Booking Type:  \t\t',y)
print ('Amt Before Discount:  \t',c)
print ('Discount:  \t\t',d)
print ('Amount Payable:  \t',b)

