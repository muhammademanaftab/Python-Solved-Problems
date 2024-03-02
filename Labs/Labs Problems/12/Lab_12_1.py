
from random import *
LENGTH = randint(5,9)
d = [[randint(1,9) for i in range(LENGTH)] for j in range(LENGTH)]
for i in range(LENGTH):                
     d[i][i] = 0  
for i in range (LENGTH):
    for j in range (LENGTH):
        print (d[i][j],end=' ')
    print()
c1=randint (0,LENGTH-1)
print(c1)


c2=randint (0,LENGTH-1)  
print(c2)
def distance (d,c1,c2): 
    print ('Direct Distance:',d[c1][c2])
    for i in range (LENGTH):
        if i!=c1 and i!=c2:
            print ( f'Via City {i}:',d[c1][i] + d[i][c2])    
distance(d,c1,c2)
           