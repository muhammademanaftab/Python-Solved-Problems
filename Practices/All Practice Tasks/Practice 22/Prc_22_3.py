from random import *
def main():
    f1=open('marks2.txt','w')
    classes=5
    f1.write(str('Classes:  ')+str(classes)+'\n')
    for i in range (1,classes+1):
        f1.write(str(f'Class {i}: ')+'\n')
        students=randint(7,10)
        f1.write(str ('Students:  ')+str (students)+'\n')
        f1.write(str('Marks:  '))
        for j in range (students):
            marks=randint(0,100)
            f1.write (str(marks)+'  ')
        f1.write('\n')
main()
            
