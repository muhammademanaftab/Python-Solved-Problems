def main():
    f1=open('marks.txt','r')
    f2=open('marks_appear.txt','w')
    students=int(f1.readline())
    subject=0
    for i in range (students):
        rollno=int(f1.readline())
        j=1
        while j<=4:
            numbers=int(f1.readline())
            if numbers==-1:
                subject=subject
            elif numbers==-2:
                subject=subject
            else:                    
                subject=subject+1
            j=j+1
            if numbers == -2:
                j=5
    f2.write(str(subject)+'\n')
    f1.close()
    f1=open('marks.txt','r')
    students=int(f1.readline())
    for i in range (students):
        rollno=int(f1.readline())
        f2.write(str(rollno)+'\n')
        j=1
        while j<=4:
            numbers=int(f1.readline())
            if numbers==-1:
                subject=subject
                f2.write(f'Not Appeared in {j} exam'+'\n')
            elif numbers==-2:
                f2.write(str('Absent')+'\n')
                
            else:                    
                subject=subject+1
                f2.write (str(numbers)+'\n')
            j=j+1
            if numbers == -2:
                
                j=5
main()

            
        
        
        
