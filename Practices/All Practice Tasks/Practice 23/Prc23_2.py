def main():
    f1=open('matrix1.txt','r')
    f2=open('matrix2.txt','r')
    f_add=open('sum.txt','w')
    f_diff=open('diff.txt','w')
    count_1=int(f1.readline())
    count_2=int(f2.readline())
    for i in range (count_1):
        r=int(f1.readline())
        r=int(f2.readline())
        c=int(f2.readline())
        c=int(f1.readline())
        f_add.write(str('Rows:  ')+str(r)+str('\t\t')+str('Columns:  ')+str('c')+'\n')
        f_diff.write(str('Rows:  ')+str(r)+str('\t\t')+str('Columns:  ')+str('c')+'\n')
        for j in range (r):
            for k in range (c):                
                value1=int(f1.readline())
                value2=int(f2.readline())
                add=value1+value2
                diff=value1-value2
                f_add.write (str(add)+'\n')
                f_diff.write(str(diff)+'\n')
    f1.close()
    f2.close()
    f_add.close()
    f_diff.close()
main()
        
