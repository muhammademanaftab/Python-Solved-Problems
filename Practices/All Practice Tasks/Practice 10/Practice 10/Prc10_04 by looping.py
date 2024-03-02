def main():
    i=1
    l=-99999
    while i<=5:
        n=int(input( 'Number:  '))
        if n>l:
            l=n
        i=i+1
    print (f'largest number:  {l}')
            
main()        
        
