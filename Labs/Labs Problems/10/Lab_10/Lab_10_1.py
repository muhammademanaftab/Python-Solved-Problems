from random import *
def main():
    x=[1]*12
    print ('Monthly Sales:',end='')
    overall_min=0
    overall_max=0
    min_index=0
    index_min=0
    max_index=0
    index_max=0
    min_avg=0
    max_avg=0
    avg_max=0
    avg_min=0
    for i in range (12):
        x[i]=randint(10,99)
        if i==0:
            overall_min=overall_max=x[i]
        elif overall_min>x[i]:
            overall_min=x[i]
        elif overall_max<x[i]:
            overall_max=x[i]
        print (x[i],end='  ')
    print()
    print ('Quarter 1:',end='')
    min=0
    max=0
    sum=0
    average=0
    for i in range (3):
        print (x[i],end='  ')
        if i==0:
            max=min=x[i]
            min_index=x[i]
        if min>x[i]:
            min=x[i]
        if max<x[i]:
            max=x[i]
        sum=sum+x[i]
        if min_index>x[i]:
            min_index=x[i]
            index_min=1
        if max_index<x[i]:
            max_index=x[i]
            index_max=1
    average=sum//3
    print ('Min:',min,end='  ')        
    print ('Max:',max,end='  ')     
    print ('Average:',average,end='  ')
    print()
    min=0
    max=0
    average_1=0
    sum_1=0
    print ('Quarter 2:',end='')
    for i in range (3):
        print (x[i+3],end='  ')
        sum=sum+x[i+3]
        if i==0:
            min=max=x[i+3]
        if min>x[i+3]:
            min=x[i+3]
        if max<x[i+3]:
            max=x[i+3]
        if min_index>x[i+3]:
            min_index=x[i+3]
            index_min=2
        if max_index<x[i+3]:
            max_index=x[i+3]
            index_max=2
        sum_1=sum_1+x[i+3]
    average_1=sum_1//3
    print ('Min:',min,end='  ')        
    print ('Max:',max,end='  ')     
    print ('Average:',average_1,end='  ')
    print()
    min=0
    max=0
    average_2=0
    sum_2=0
    print ('Quarter 3:',end='')
    for i in range (3):
        print (x[i+6],end='  ')
        sum=sum+x[i+6]
        if i==0:
            min=max=x[i+6]
        if min>x[i+6]:
            min=x[i+6]
        if max<x[i+6]:
            max=x[i+6]
        if min_index>x[i+6]:
            min_index=x[i+6]
            index_min=3
        if max_index<x[i+6]:
            max_index=x[i+6]
            index_max=3
        sum_2=sum_1+x[i+6]
    average_2=sum_2//3
    print ('Min:',min,end='  ')        
    print ('Max:',max,end='  ')     
    print ('Average:',average_2,end='  ')
    print()
    min=0
    max=0
    average_3=0
    sum_3=0
    print ('Quarter 4:',end='')
    for i in range (3):
        print (x[i+9],end='  ')
        sum=sum+x[i+9]
        if i==0:
            min=max=x[i+9]
        if min>x[i+9]:
            min=x[i+9]
        if max<x[i+9]:
            max=x[i+9]
        if min_index>x[i+9]:            
            index_min=4
        if max_index<x[i+9]:
            max_index=x[i+9]
            index_max=4
        sum_3=sum_3+x[i+9]
    average_3=sum_3//3        
    print ('Min:',min,end='  ')        
    print ('Max:',max,end='  ')     
    print ('Average:',average_3,end='  ')
    print()
    if average>average_1 and average>average_2 and average>average_3:
        max_avg=1
        avg_max=average
    if average_1>average and average_1>average and average_1>average_3:
        max_avg=2
        avg_max=average_1
    if average_2>average_1 and average_2>average and average_2>average_3:
        max_avg=3
        avg_max=average_2
    if average_3>average_1 and average_3>average_2 and average_3>average:
        max_avg=4
        avg_max=average_3



    if average<average_1 and average<average_2 and average<average_3:
        min_avg=1
        avg_min=average
    if average_1<average and average_1<average and average_1<average_3:
        min_avg=2
        avg_min=average_1
    if average_2<average_1 and average_2<average and average_2<average_3:
        min_avg=3
        avg_min=average_2
    if average_3<average_1 and average_3<average_2 and average_3<average:
        min_avg=4
        avg_min=average_3
    print (f'Quarter {index_min} has minimum sale {overall_min}')
    print (f'Quarter {index_max} has maximum sale {overall_max}')
    print (f'Quarter {max_avg} has maximum average sale {avg_max}')    
    print (f'Quarter {min_avg} has minimum average sale {avg_min}')
    
main()

    
        
            
    

            
        
