
from random import *
LENGTH = randint(5,9)
d = [[randint(1,9) for i in range(LENGTH)] for j in range(LENGTH)]
for j in range (LENGTH):
        i=randint(1,5)
        j=randint(1,5)
        d[i][j]=-1
for i in range(LENGTH):                
     d[i][i] = 0  
for i in range (LENGTH):
    for j in range (LENGTH):
        print (d[i][j],end='  ')
    print()
print()

c1=randint (0,LENGTH-1)
c2=randint (0,LENGTH-1)  
def distance (d,c1,c2): 
    for i in range (LENGTH):
        print(f'City {i} has direct link with : ',end='  ')       
        for j in range (LENGTH):                     
            if i!=j and d[i][j]!=-1:  
                print (j ,end=' ' )
        print()
      
distance(d,c1,c2)
           