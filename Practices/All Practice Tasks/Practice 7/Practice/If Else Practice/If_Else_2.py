x= int (input ('Classes Held:  '))
y= int (input ('Classes Attend:  '))
z=y/x
c=z*100
print ('Percenatge of Classes Attend:  ',c)
if c>=75:
    print ('Allowed to Sit')
else:
    print ('Not Allowed to sit')
