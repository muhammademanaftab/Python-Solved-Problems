def return_function (a,b,c):
    if a>b and a<c:
        return a
    if b>a and b<c:
        return  b
    if c>a and c<b:
        return c
    if a>c and a<b:
        return a
    if b>c and b<a:
        return b
    if c>b and c<a:
        return c

m=int(input('First Number:  '))
n=int(input('Second Number:  '))
p=int(input('Third Number:  '))
    
print (return_function(m,n,p))
