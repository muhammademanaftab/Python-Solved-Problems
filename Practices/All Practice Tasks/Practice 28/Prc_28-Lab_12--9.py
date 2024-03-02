from random import *
def main():
    x=[3,2,0,1,2,4,6,2,1,9,8,2,3,4,6,2,0,1,3,4]
    print('List: ',x)


    # for i in range (len(x)):
    #     x[i]=randint(0,9)
    #     print(x[i],end=' ')
    # print()


    print('Output: ',end='')
    for i in range (2):
        print (x[i],end=' ')

    for i in range (len(x)):
        sum=0
        avg=0
        if i>=2 and i<=17:
            sum=(x[i-2])+(x[i-1])+(x[i+1])+(x[i+2])
            avg=sum//4
            print(avg,end=' ')

    j=len(x)-2
    while j<len(x):
        print (x[j],end=' ')
        j=j+1
main()