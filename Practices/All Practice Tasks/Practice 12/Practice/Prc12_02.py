def main():
    x=int(input(''))
    l=1
    y=1
    z=1
    while l<=x:
        A=y+64
        y=y+1        
        capital_alphabets=chr(A)
        print (f'{capital_alphabets}',end=' ')
        B=123-z
        z=z+1
        small_alphabets=chr(B)
        print (f'{small_alphabets}',end=' ')

        l=l+1
main()    
        
        
