def main():
    i=1
    while i<=100:
        
        if i%3==0 or i%5==0:
            
            if i%3==0 and i%5==0:
                
                i=i+1
            else:
                
                print (i, end=' ')
                
                i=i+1
        else:
            
            i=i+1
main()
