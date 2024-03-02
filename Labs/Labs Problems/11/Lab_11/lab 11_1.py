from random import *
def main():
    x=[0]*10
    length=10
    for i in range (length):
        x[i]=randint(10,99)
    y=[x[i] for i in range (len(x))]
    print (y)
    for i in range (length):                
        for j in range (length):
            if j!= length-1:                    
                if y[j]>y[j+1]:
                    y[j],y[j+1]=y[j+1],y[j]
                print (y[j],end=' ')
            elif j== length-1:
                print (y[j])            
    print ('-------------------')
    for i in range (length):
        print (f'{x[i]} is at position ',end='')
        j=1
        for j in range (length) :
            if x[i]==y[j] :
                print (j,end=' ')
            
                
        print()
            
                
main()
