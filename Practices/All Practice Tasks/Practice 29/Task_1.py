def main():
    f1=open('paragraph.txt','r')
    sent=f1.readline()
    count=0
    for i in range (len(sent)):
        if sent[i]==' ' :
            count+=1
    print('Total Words: ',(count+1))
    
main()