from random import *
LENGTH = randint(5,9)
d = [[randint(1,9) for i in range(LENGTH)] for j in range(LENGTH)]
for i in range(LENGTH):                
     d[i][i] = 0  
for i in range (LENGTH):
    for j in range (LENGTH):
        print (d[i][j],end='  ')
    print()
def distance (d): 
    min=0
    d1=0
    d2=0
    for i in range (LENGTH):         
         for j in range (LENGTH):
               if i==0 and j==1:
                    min=d[i][j]
               elif d[i][j] < min and d[i][j]!=0:
                    min=d[i][j]
                    d1=i
                    d2=j
    print ('Shortest Distance:',min)
    print ('City 1:',d1)
    print ('City 2:',d2)
distance(d)


                    
                