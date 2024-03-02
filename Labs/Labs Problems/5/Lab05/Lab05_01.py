from random import *
x=randint (20,99)
y=x//10
z=x%10

if z==1:
    a='One'
elif z==2:
    a='two'    
elif z==3:
    a='three'
elif z==4:
    a='four'
elif z==5:
    a='five'
elif z==6:
    a='six'
elif z==7:
    a='seven'
elif z==8:
    a='eight'    
elif z==9:
    a='nine'
    
if x>20 and x<30:
    print (f'Number {x} in English is twenty-{a}')
elif x==20:
    print (f'Number {x} in English Twenty')
elif x>30 and x<40:
    print (f'Number {x} in English is thirty-{a}')
elif x==30:
    print (f'Number {x} in English Thirty')    
elif x>40 and x<50:
    print (f'Number {x} in English is fourty-{a}')
elif x==40:
    print (f'Number {x} in English Fourty')    
elif x>50 and x<60:
    print (f'Number {x} in English is fifty-{a}')
elif x==50:
    print (f'Number {x} in English Fifty')    
elif x>60 and x<70:
    print (f'Number {x} in English is sixty-{a}')
elif x==60:
    print (f'Number {x} in English Sixty')    
elif x>70 and x<80:
    print (f'Number {x} in English is seventy-{a}')
elif x==70:
    print (f'Number {x} in English Seventy')
elif x>80 and x<90:
    print (f'Number {x} in English is eighty-{a}')
elif x==80:
    print (f'Number {x} in English Eighty')    
elif x>90 and x<99:
    print (f'Number {x} in English is ninety-{a}')
elif x==90:
    print (f'Number {x} in English Ninety')    
    
    
