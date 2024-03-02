def main():
    f1=open('marks.txt','r')
    students=int(f1.readline())
    print (students)
    sum=0
    for i in range (students):
        rollno=int(f1.readline())
        j=1
        while j<=4:
            numbers=int(f1.readline())
            j=j+1
            if numbers == -2:
                j=5            
        if numbers==-2:
            sum=sum
        else:
            sum=sum+1
    print ('Students Apperead in Exam:',sum)
main()

            
        
        
        
