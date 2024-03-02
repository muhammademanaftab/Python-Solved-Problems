def main():
    x=int(input('Input Format\n'))
    print('Constraints\nPositive integer only')
    y=1    
    l=1    
    
    while l<=x:
        A=y+64
        y=y+1        
        capital_alphabets=chr(A)        
        print (f'{capital_alphabets}',end='')        
        l=l+1
    print()

    z=1
    m=1
    a=x
    while m<=a:
        B=z+96
        z=z+1       
        small_alphabets=chr(B)        
        print (f'{small_alphabets}',end='')        
        m=m+1
        

main()        
          
