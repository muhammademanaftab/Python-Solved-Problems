def main():
    x=int(input('Enter Number:  '))
    sum=0
    average=0
    count = 0
    if x>0:
        while x>0:
            sum = sum+x
            count=count+1
            average= sum / count
            x=int(input('Enter Number:  '))
        print ('Sum:  ',sum)
        print ('Average:  ',average)
main( )
             
            
