from random import *
def main ():
    l=1
    while l<=10:
        n=randint (1,100)
        b=n%10
        print (f'Number in digits:  {n}')
        print (f'Number in words:  ', end= ' ')
        # If n < 10 Than We Use:
        if n==1 or b==1:
            x='One'
        elif n==2 or b==2:
            x='Two'
        elif n==3  or b==3:
            x='Three'
        elif n==4  or b==4:
            x='Four'
        elif n==5  or b==5:
            x='Five'
        elif n==6  or b==6:
            x='Six'
        elif n==7  or b==7:
            x='Seven'
        elif n==8  or b==8:
            x='Eight'
        elif n==9  or b==9:
            x='Nine'
        elif n==0:
            x=' '        


        if n<10:
            print (f'{x}')
        elif n==10:
            print ('Ten')
        elif n==11:
            print ('Eleven')
        elif n==12:
            print ('Twelve')
        elif n==13:
            print ('Thirteen')
        elif n==14:
            print ('Fourteen')
        elif n==15:
            print ('Fifteen')
        elif n==16:
            print ('Sixteen')
        elif n==17:
            print ('Seventeen')
        elif n==18:
            print ('Eighteen')
        elif n==19:
            print ('Ninteen')
        
        elif n>=20 and n<30:
            print (f'Twenty {x}')
        elif n>=30 and n<40:
            print (f'Thirty {x}')
        elif n>=40 and n<50:
            print (f'Fourty {x}')
        elif n>=50 and n<60:
            print (f'Fifty {x}')
        elif n>=60 and n<70:
            print (f'Sixty {x}')
        elif n>=70 and n<80:
            print (f'Seventy {x}')
        elif n>=80 and n<90:
            print (f'Eighty {x}')
        elif n>=90 and n<100:
            print (f'Ninty {x}')
        elif n==100:
            print ('Hundred')
        print()        
        l=l+1

main()            
