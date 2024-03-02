from random import *
n1=randint(1,100)
n2=randint(1,100)
n3=n1
if n1>n2:
    n1,n2=n2,n1
    
while n1<=n2:
    print (n1, end =' ')
    n1=n1+1
    
print()
while n2>=n3:
    print (n2, end =' ')
    n2=n2-1
