def main():
    i=1
    b=0
    print (' ', end='')
    while i<=100:
        if b<5:
            b=b+1
            print (i, end=' ')
            i=i+1            
        else:
            b=1           
            print('\n',i, end=' ')
            i=i+1
           

main()             
