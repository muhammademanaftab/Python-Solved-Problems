def main():
    x=1    
    while x<=99:
        if x<10:
            print (f'[{x}]', end =' ')
        if x>10:
            a=x//10
            b=x%10
            s=a+b
            if s<10:
                print (f'[{x} {s}]', end =' ')
            if s>10:
                n=s//10
                m=s%10
                s1=n+m
                print (f'[{x} {s} {s1}]',end=' ')
        x=x+1        
main()            
            
            
