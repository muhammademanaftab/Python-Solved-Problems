def main():
    f1=open('letters.txt','r')
    A=0
    B=0
    i=1
    while i<=10000:
        n=(f1.readline().strip('\n'))
        if n=='A' or n=='a':
            A=A+1
        elif n=='B'or n=='b':
            B=B+1
        i=i+1
    print ('Count Of A:  ',A)
    print ('Count Of B:  ',B)

main()    
        
              
