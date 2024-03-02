from random import *
def main(n):
    for j in range (1,n+1):
        print (f'Over {j}:  ',end=' ')
        score=0
        wickets=0
        balls=6
        for i in range (1,balls):
            ball=randint(0,9)
            if ball >=0 and ball<=6:
                print (ball,end=' ')
                score=score+ball                    
            elif ball==7:                    
                print('W',end=' ')
                
                score=score+1
            elif ball==8:
                out=randint(1,3)
                wickets=wickets+1
                if out==1:
                    print ('R',end=' ')
                if out==2:
                    print ('B',end=' ')
                if out==3:
                    print ('C',end=' ')
            elif ball==9:
                    print ('N',end=' ')
                     
        print('\t\t',end=' ')
        print ('Total:',score,end='\t\t')
        print ('Wickets:  ',wickets)

main(6)
        
        
