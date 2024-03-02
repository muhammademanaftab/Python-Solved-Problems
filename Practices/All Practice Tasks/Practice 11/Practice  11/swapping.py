from random import *
def main():
    n1=randint(1,1000)
    n2=randint(1,1000)
    n3=randint(1,1000)
    n4=randint(1,1000)
    print ('Number Before Ordering:  ', n1 , n2 , n3 , n4 )
    if n1>n2: n1,n2=n2,n1;
    if n2>n3: n2,n3=n3,n2;
    if n3>n4: n3,n4=n4,n3;
    if n1>n2: n1,n2=n2,n1;
    if n2>n3: n2,n3=n3,n2;
    if n1>n2: n3,n4=n4,n3;
    print ('Number after ordering:  ', n1 , n2 , n3 ,n4)
main()
