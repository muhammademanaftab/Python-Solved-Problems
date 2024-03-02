def main():
    f1=open('marks.txt','r')
    students=int(f1.readline())
    print (students)
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
    print ('Appreaed in All Subjects:',subject)   
main()

            
        
        
        
