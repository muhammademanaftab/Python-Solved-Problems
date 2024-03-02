from random import *
def main():
    i=0
    cs=0
    ma=0
    sa=0
    f=0
    p=0
    af=0
    maxtotal=0
    maxmid=0
    maxsessional=0
    maxfinal=0
    mintotal=101
    minmid=101
    minsessional=101
    minfinal=101
    
    while i<30:
        midterm=randint(1,35)
        finalterm=randint(1,40)
        
        sessional=randint(1,25)
        sum=midterm+finalterm+sessional
        if sum>maxtotal:
            maxtotal=sum
        if midterm>maxmid:
            maxmid=midterm
        if finalterm>maxfinal:
            maxfinal=finalterm
        if sessional>maxsessional:
            maxsessional=sessional

        if sum<mintotal:
            mintotal=sum
        if midterm<minmid:
            minmid=midterm
        if sessional<minsessional:
            minsessional=sessional
        if finalterm<minfinal:
            minfinal=finalterm
            
        if sum>90:
            Grade='A+'
        elif sum>85 :
            Grade='A'
        elif sum >80 :
            Grade= 'B+'
        elif sum >70 :
            Grade= 'B-'
        elif sum >65 :
            Grade= 'C'
        elif sum >60 :
            Grade= 'D'
        elif sum >55 :
            Grade= 'E '
        elif sum <50:
            Grade= 'F'
        if sum<=50:
            f=f+1
        else:
            p=p+1
           
            
        

        print ( 'Roll No \t Mid \t Final \t Sessional \t Total \t Grade')
        cs=cs+sum        
        ma=ma+midterm
        sa=sa+sessional
        af=af+finalterm
        
        i=i+1
        
        
        print (i,'\t\t',midterm,'\t',finalterm,'\t',sessional,'\t\t',sum,'\t',Grade)
    overall_average=cs/30
    ma=ma/30
    sa=sa/30
    af=af/30
    print (f'Pass:  {p}')
    print (f'Fail:  {f}')
    print ('Overall Average Marks:  ',overall_average)
    print('Average Midterm: ',ma)
    print ('Sessional Average:  ',sa)
    print ('Final Term Average Marks  ',af)
    print ('Max Marks:  ',maxtotal)
    print ('Max Final:  ', maxfinal)
    print ('Max Mid:  ',maxmid)
    print ('Max Sessional:  ',maxsessional)
    print ('Minimum Marks:  ',mintotal)
    print ('Minimum Mid Term Marks:  ',minmid)
    print ('Minimum Sessional Marks:  ',minsessional)
    print ('Minmum Final term Marks:  ',minfinal)

    
main()        
          
            
        
