def main():
    f1=open ('nums.txt','r')
    i=1
    count_1=0
    count_2=0
    count_3=0
    count_4=0
    count_5=0
    count_6=0
    count_7=0
    count_8=0
    count_9=0
    while i<=10000:
        n=int(f1.readline())
        if n==1:
            count_1=count_1+1
        elif n==2:
            count_2=count_2+1
        elif n==3:
            count_3=count_3+1
        elif n==4:
            count_4=count_4+1
        elif n==5:
            count_5=count_5+1
        elif n==6:
            count_6=count_6+1
        elif n==7:
            count_7=count_7+1
        elif n==8:
            count_8=count_8+1
        elif n==9:
            count_9=count_9+1

        i=i+1
    print ('Count 1:  ',count_1)
    print ('Count 2:  ',count_2)
    print ('Count 3:  ',count_3)
    print ('Count 4:  ',count_4)
    print ('Count 5:  ',count_5)
    print ('Count 6:  ',count_6)
    print ('Count 7:  ',count_7)
    print ('Count 8:  ',count_8)
    print ('Count 9:  ',count_9)

main()    
    
