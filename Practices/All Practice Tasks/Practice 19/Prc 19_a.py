def even_numbers (n):
    i=1
    a=0
    while i<=n:
        a=a+2
        print (a,end=' ')
        i=i+1

m=input('Wanna Call The Function Y/N :')
if m=='Y' or m=='y':
    n=int(input('Number:  '))
    even_numbers(n)
