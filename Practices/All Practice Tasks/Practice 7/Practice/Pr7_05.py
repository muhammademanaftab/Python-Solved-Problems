x= int (input ('Enter Number'))
a=x%2
b=x%3
c=x%5
d=x%7
if a==0 and b==0 and c==0 and d==0:
    print ('Number is divisible by 2,3,5,7')
elif a==0 and b==0 and c==0:
    print ('Number is divisble by 2,3,5')
elif a==0 and b==0:
    print ('Number is divisible by 2,3')
elif a==0 and c==0:
    print ('Number is divisible by 2,5')
elif a==0 and d==0:
    print('Number is divisible by 2,7')
elif b==0 and c==0 and d==0:
    print ('Number is divisible by 3,5,7')
elif b==0 and c==0:
    print ('Number is divisible by 3,5')
elif b==0 and d==0:
    print('Number is divisible by 3,7')
elif c==0 and d==0:
    print ('Number is divisible by 5,7')
elif a==0:
    print ('Number is divisible by 2')
elif b==0:
    print ('Number is divisible by 3')
elif c==0:
    print ('Number is divsibile by 5')
else:
    print ('Number is divisible by 7')

