def main():
    r=int(input('Rows:  '))
    for i in range (r):
        for j in range (i):
            print (' ',end='')
        print ('\\')
    for k in range (r):
        print (' ',end='')
    for l in range (r):
        print ('-',end='')
    print()
    for m in range (r):
        for n in range (r-m,1,-1):
            print(' ',end='')
        print ('/')
main()

def while_loop ():
    r=int(input('Rows:  '))
    i=1
    while i<=r:
        j=1
        while j<i:
            print (' ',end='')
            j=j+1
        print ('\\')
        i=i+1
    k=1
    while k <=r:
        print (' ',end='')
        k=k+1
    m=1
    while m<=r:
        print ('-',end='')
        m=m+1
    print()
    n=1
    while n<=r:
        o=n
        while o < r:
            print (' ',end='')
            o=o+1
        print ('/')
        n=n+1
print()
print()
while_loop()
