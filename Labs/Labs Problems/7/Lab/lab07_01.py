from random import *
def main():
    i=1
    marks=0
    while i<=10:
        A=randint(1,3)
        x=randint(0,99)
        y=randint(0,99)
        a=randint(10,99)
        b=randint(1,9)
        c=randint(0,9)
        d=randint(0,9)
        a=x+y
        s=a-b
        n=c*d
        
        
        
        if A==1:            
            print('Subtraction')
            print (f'N1: {a}', end=' ')
            print (f'N2: {b}')
            m=int(input('Answer:  '))
            
            if s==m:
                print('Correct')
                marks=marks+3
                i=i+1
            else:
                print('Incorrect')
                i=i+1

        if A==2:
            print ('Addition')
            print (f'N1: {x}', end=' ')
            print (f'N2: {y}')
            m=int(input('Answer:  '))
            
            if a==m:
                print('Correct')
                marks=marks+3
                i=i+1
            else:
                print ('Incorrect')
                i=i+1

        if A==3:
            print ('Multiplication')
            print (f'N1: {c}', end=' ')
            print (f'N2: {d}')
            m=int(input('Answer:  '))
            
            if n==m:
                print ('Correct')
                marks=marks+3
                i=i+1

            else:
                print ('Incorrect')
                i=i+1
        
    print('Marks:  ', marks)

main()        
        
        
        
