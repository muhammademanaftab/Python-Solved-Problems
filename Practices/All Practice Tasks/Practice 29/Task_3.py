def main():
    f1=open('paragraph.txt','r')
    sent=f1.readline()
    count=0
    for i in range (len(sent)):
        if sent[i]=='.' and count==0:
            j=0
            while sent[j]!='.':
                print(sent[j],end='')
                j=j+1
            count+=1
            print('.')
            
        elif sent[i]=='.':
            j=i+1
            while j!=len(sent) and sent[j]!='.' :
                print(sent[j],end='')
                j=j+1
            count+=1
            print('.')
    print('Total Senteneces: ',(count-1))
main()