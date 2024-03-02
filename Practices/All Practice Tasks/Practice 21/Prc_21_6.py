from random import *
def main():
    i=0
    sum=0
    while i<=1:
        x= randint (1,10)
        sum = sum+x
        print (x, end='  ')
        if sum == 50:
            i=i+1
            print ('Sum:',sum, end='      ')
            sum=0
            print ('---------Found-------')
        if sum > 50:
            print ('Sum:',sum,end='       ')
            sum=0
            print ('Not Found Yet')
            print ('Again Generation:  ')
main()
    
        
