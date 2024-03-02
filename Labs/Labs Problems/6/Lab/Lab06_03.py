from random import *
def main():
    l=1
    marks=0
    while l<=2:
        x=randint (1,9)
        y=randint (1,9)
        print (f'N1:{x}   N2:{y}')
        
                
        a=int (input ('Sum:  '))              
        if x+y==a:
               marks=marks+3
        else:
            a=int(input ('Wrong, Enter Sum Again:  '))
            if x+y==a:
                marks=marks+3
            else:
                a=int(input ('Again Wrong, Last Chance To Enter Sum:  '))
                if x+y==a:
                    marks=marks+3


        b=int (input ('Difference:  '))
        if x-y==b:
               marks=marks+3
        else:
            a=int(input ('Wrong, Enter Difference Again:  '))
            if x-y==b:
                marks=marks+3
            else:
                a=int(input ('Again Wrong, Last Chance To Enter Difference:  '))
                if x-y==b:
                    marks=marks+3            
                    

        c=int (input ('Product:  '))
        if x*y==c:
               marks=marks+3
        else:
            a=int(input ('Wrong, Enter Product Again:  '))
            if x*y==c:
                marks=marks+3
            else:
                a=int(input ('Again Wrong, Last Chance To Enter Product:  '))
                if x*y==c:
                    marks=marks+3

        
       

       

        l=l+1
    print (' Obtained Marks:  ',marks)

main()        

                    
                
