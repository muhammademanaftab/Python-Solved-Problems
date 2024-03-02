
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
c2=randint (0,LENGTH-1)  
def distance (d,c1,c2): 
    print ('Direct Distance:',d[c1][c2])
    direct=d[c1][c2]
    min=999999
    min_index=0
    for i in range (LENGTH):
        ind=0
        if i!=c1 and i!=c2:
            print ( f'Via City {i}:',d[c1][i] + d[i][c2])   
            ind=d[c1][i] + d[i][c2]
            if min > ind:
                 min=ind
                 min_index=i
    if direct > min:
            direct=min         

    print ('Shortest Distance:',direct)
    
distance(d,c1,c2)
           