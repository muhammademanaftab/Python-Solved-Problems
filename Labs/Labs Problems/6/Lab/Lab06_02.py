def main():
    l=1
    while l<=100:
        b=l%10
        if l==1 or b==1:
            x='One'
        elif l==2 or b==2:
            x='Two'
        elif l==3  or b==3:
            x='Three'
        elif l==4  or b==4:
            x='Four'
        elif l==5  or b==5:
            x='Five'
        elif l==6  or b==6:
            x='Six'
        elif l==7  or b==7:
            x='Seven'
        elif l==8  or b==8:
            x='Eight'
        elif l==9  or b==9:
            x='Nine'
        elif b==0:
            x=' '        


        if l<10:
            print (f'{x}')
        elif l==10:
            print ('Ten')
        elif l==11:
            print ('Eleven')
        elif l==12:
            print ('Twelve')
        elif l==13:
            print ('Thirteen')
        elif l==14:
            print ('Fourteen')
        elif l==15:
            print ('Fifteen')
        elif l==16:
            print ('Sixteen')
        elif l==17:
            print ('Seventeen')
        elif l==18:
            print ('Eighteen')
        elif l==19:
            print ('Ninteen')
        
        elif l>=20 and l<30:
            print (f'Twenty {x}')
        elif l>=30 and l<40:
            print (f'Thirty {x}')
        elif l>=40 and l<50:
            print (f'Fourty {x}')
        elif l>=50 and l<60:
            print (f'Fifty {x}')
        elif l>=60 and l<70:
            print (f'Sixty {x}')
        elif l>=70 and l<80:
            print (f'Seventy {x}')
        elif l>=80 and l<90:
            print (f'Eighty {x}')
        elif l>=90 and l<100:
            print (f'Ninty {x}')
        elif l==100:
            print ('Hundred')
                
        l=l+1

main()            
                
                
                
                
