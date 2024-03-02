def distance_function(n,d):
    i=1
    m=1
    while i<=n:
        print (m,end=' ')
        m=m+d
        i=i+1
s=input('Wanna call function Y/N:  ')
if s=='Y' or s=='y':
    n=int(input('Count:  '))
    d=int(input('Distance:  '))
    print (distance_function (n,d))
