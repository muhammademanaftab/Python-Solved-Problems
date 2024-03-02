from random import *
def main():
    i=1
    smallest=0
    second_smallest=0
    while i<=10:
        x=randint(1,20)
        print(x)
        if i==1:
            smallest=x
            second_smallest=x       
        if x<smallest:
            second_smallest=smallest
            smallest=x
        elif smallest==second_smallest:
            second_smallest=x
        elif x<second_smallest and x>smallest:            
            second_smallest=x    
        i=i+1
    print('Smallest:  ',smallest)
    print('Second_smallest:  ',second_smallest)
main()

        
