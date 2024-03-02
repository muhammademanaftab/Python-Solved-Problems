def main():
    f1=open('marks.txt','r')
    students=int(f1.readline())
    print ('Total Students:', students)
    roll_no=int(input('Enter Roll No:'))
    for i in range (students):
        roll=int(f1.readline())        
        if roll==roll_no:
            numbers=int(f1.readline())
            if numbers==-2:
                print ('Student is absent')
            else:
                print ('Marks:','\t',end='')
                j=1
                sum=0
                count=0
                average=0
                while j<=4:                    
                    print (numbers,'\t',end='')
                    if numbers==-1:
                        print('Not Appeared in Exam')                        
                    else:
                        sum=sum+numbers
                        count=count+1
                    numbers=int(f1.readline())
                    j=j+1
                average=sum//count
                print('Average:',average)
        j=1
        while j<=4:
            numbers=int(f1.readline())
            j=j+1
            if numbers == -2:
                j=5
        
main()

            
        
        


            
        
        
