def print_chr (c,n):
    i=1
    while i<=n:
        print (c,end=' ')
        i=i+1
m=input('Call the function:  ')
if m=='y' or m=='Y':
    n=int(input('Count:  '))
    c=input('Character:  ')
    print_chr(c,n)
        
