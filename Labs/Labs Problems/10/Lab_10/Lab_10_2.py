from random import *
def main():
    x=[1]*10
    y=[1]*10
    z=[1]*10
    b=0
    score=0
    for i in range (10):
        x[i]=randint (1,9)
        y[i]=randint(1,9)
        a=int(input(f'{x[i]}+{y[i]} ='))
        z[i]=a
        b=(x[i]+y[i])
        if b==z[i]:
            score=score+1        
    print(f'Score  {score}/10')
    print ('InCorrect:','\t','Correct:')
    for i in range (10):
        b=x[i]+y[i]
        if b!=z[i]:
            print (f'{x[i]}+{y[i]}={z[i]}',end='\t\t ')
            print (f'{x[i]}+{y[i]}={b}')
main()
