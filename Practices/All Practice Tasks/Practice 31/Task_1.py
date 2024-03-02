def main():
    f1=open('nums.txt','r')
    f2=open('sum.txt','w')
    values=f1.readline()
    f2.write(str(values))
    list1 = list(map(int, f1.readline().split()))
    list2 = list(map(int, f1.readline().split()))
    for i in range (int (values)):
        f2.write(str(list1[i]+list2[i])+' ')
main()