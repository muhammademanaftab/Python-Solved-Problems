def main():
    f1=open('nums.txt','r')
    f2=open('compare.txt','w')
    values=f1.readline()
    f2.write(str(values))
    list1 = list(map(int, f1.readline().split()))
    list2 = list(map(int, f1.readline().split()))
    for i in range (int (values)):
        if list1[i]==list2[i]:
            f2.write(str('1')+' ')
        else:
            f2.write(str('0')+' ')
main()