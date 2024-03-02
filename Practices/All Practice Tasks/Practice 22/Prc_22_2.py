def main():
    f1=open('marks.txt','r')
    f2=open('marks1.txt','w')
    count_1=int(f1.readline())
    f2.write(str(count_1)+'\n')
    for i in range (count_1):
        count_2=int(f1.readline())
        f2.write(str(count_2)+'\n')
        for j in range (count_2):
            marks=int(f1.readline())
            f2.write (str(marks)+' ')
        f2.write('\n')
    f1.close()
    f2.close()
main()
