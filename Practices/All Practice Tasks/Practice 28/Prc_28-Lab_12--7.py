from random import *
def main():
    x = [0]*10
    print('List:', end='')
    for i in range(len(x)):
        x[i] = randint(1, 5)
        print(x[i], end=' ')
    print()
    for i in range (len(x)):
        print (f'{x[i]} at position',end=' ')
        # if x[i]!=-1 :
        #     print()
        #     print (f'{x[i]} is at position: ',end='')
        # for j in range (i+1,len(x)):
        #     if x[i]==x[j] and x[i]!=-1:
        #         x[j]=-1
        #         print (j,end=' ')
        for j in range (len(x)):
            if x[i]==x[j]:
                print (j,end=' ')
        print()
  
                
                    

main()