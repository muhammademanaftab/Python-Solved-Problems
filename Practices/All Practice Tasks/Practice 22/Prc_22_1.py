def main():
    f1=open('marks.txt','r')
    count_1=int(f1.readline())
    max_average=0
    min_average=0
    max_class=0
    min_class=0   
    for i in range (1,count_1+1):
        if i==1:
            max_average=max_class=min_class=0
            min_average=999999
        count_2=int(f1.readline())
        sum=0
        for j in range (count_2):
            number=int(f1.readline())
            sum=sum+number
        average=sum//count_2
        if average > max_average:
            max_average=average
            max_class=i
        if min_average > average:
            min_average=average
            min_class=i           
    print ('Max Average Class:','\t',max_class, end='\t')
    print ('Max Average:','\t', max_average)
    print ('Min Average Class:','\t',min_class, end='\t')
    print ('Min Average:','\t',min_average)
            
main()
