from random import *
def main():
    f1=open('matrix.txt','w')
    r=randint(4,8)
    c=randint(4,8)
    f1.write(str('Rows:  ')+str(r)+'\n')
    f1.write(str('Columns:  ')+str(c)+'\n')
    for i in range (r):
        for j in range (c):
            e=randint(1,9)
            f1.write(str(e)+' ')
        f1.write('\n')
main()
