def main():
    f1=open('marks.txt','r')
    f2=open('absent.txt','w')
    students=int(f1.readline())
    print (students)
    absent=0
    for i in range (students):
        rollno=int(f1.readline())
        j=1
        while j<=4:
            numbers=int(f1.readline())              
            j=j+1
            if numbers == -2:
                absent=absent+1
                j=5
    print ('Absent:',absent)
    f2.write(str(absent)+'\n')
    f1.close()
    f1=open('marks.txt','r')
    students=int(f1.readline())
    for i in range (students):
        rollno=int(f1.readline())
        j=1
        while j<=4:
            numbers=int(f1.readline())             
            j=j+1
            if numbers == -2:
                f2.write(str(rollno)+'\n')
                j=5
main()
