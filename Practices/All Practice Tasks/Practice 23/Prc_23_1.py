from random import *
def main():
    f1=open('matrix1.txt','w')
    f1.write(str(10)+'\n')
    f2=open('matrix2.txt','w')
    f2.write(str(10)+'\n')
    for i in range (1,11):
        r=randint(2,6)
        c=randint(2,6)
        f1.write(str(r)+'\n')        
        f2.write(str(r)+'\n')        
        f1.write(str(c)+'\n')        
        f2.write(str(c)+'\n')        
        for j in range (r):
            for k in range (c):
                e=randint(1,9)
                f=randint(1,9)
                f1.write (str(e)+'\n')
                f2.write (str(f)+'\n')
            
main()
