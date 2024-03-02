x=int(input('1st Element:  '))
y=int(input('1st Element:  '))
z=int(input('1st Element:  '))
a=int(input('1st Element:  '))
b=int(input('1st Element:  '))
d11=x-y
d12=x-z
d13=x-a
d14=x-b
d21=y-x
d22=y-z
d23=y-a
d24=y-b
d31=z-x
d32=z-y
d33=z-a
d34=z-b
d41=a-x
d42=a-y
d43=a-z
d44=a-b
d51=b-a
d52=b-y
d53=b-z
d54=b-a

print ('Difference of 1st element:  ', d11,d12,d13,d14)
print ('Difference of 2nd element:  ', d21,d22,d23,d24)
print ('Difference of 3rd element:  ', d31,d32,d33,d34)
print ('Difference of 4th element:  ', d41,d42,d43,d44)
print ('Difference of 5th element:  ', d51,d52,d53,d54)
