from random import*
s=0
i=1
while i<=10:
    c=0
    x1=randint(65,90)
    x2=randint(65,90)
    print(chr(x1),'\n',chr(x2))
    if x1&1== x2&1:
        c=c+1
        s=s+1
    if x1&2== x2&2:
        c=c+1
        s=s+1 
    if x1&4== x2&4:
        c=c+1
        s=s+1
    if x1&8== x2&8:
        c=c+1
        s=s+1
    if x1&16== x2&16 :
        c=c+1
        s=s+1
    if x1&32== x2&32 :
        c=c+1
        s=s+1
    if x1&64== x2&64 :
        c=c+1
        s=s+1
    if x1&128== x2&128 :
        c=c+1
        s=s+1
    print(f'{c} bits are same')
    i=i+1
print(f'Sum of same bits:{s}')



    
