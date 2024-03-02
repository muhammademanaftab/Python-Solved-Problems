from random import *
def main():
    for i in range (1,3):
        print (f'Team {i}')
        total=0
        result=0
        total_wickets=0
        for j in range (1,7):
            print (f'Over {j}:  ',end=' ')
            score=0
            wicket=0
            for k in range (1,7):
                ball=randint(0,9)
                if ball >=0 and ball<=6:
                    print (ball,end=' ')
                    score=score+ball                    
                elif ball==7:                    
                    print('W',end=' ')
                    score=score+1
                elif ball==8:
                    out=randint(1,3)
                    wicket=wicket+1
                    if out==1:
                        print ('R',end=' ')
                    if out==2:
                        print ('B',end=' ')
                    if out==3:
                        print ('C',end=' ')
                elif ball==9:
                        print ('N',end=' ')
            total=total+score
            total_wickets=total_wickets+wicket
            print('\t\t',end=' ')
            print ('Score:',score,end='\t\t')
            print ('Wicket:  ',wicket)            
        print ('Total:  ',total,end='\t\t')
        print ('Total Wickets:  ',total_wickets,end='\t\t')
        
        print ('\n\n')
        if result < total:
            result = i
    print (f'Result:  Winner is team {result}')
main()
