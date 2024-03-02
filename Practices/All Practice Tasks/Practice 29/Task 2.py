def main():
    f1=open('paragraph.txt','r')
    sent=f1.readline()
    max_count=0
    for i in range (len(sent)):
        count=0
        if i==0:
            j=0
            while sent[j]!=' ' :
                count+=1
                j=j+1
        
        elif sent[i]==' ':
            j=i+1
            while j!=len(sent) and sent[j]!=' ' :
                count+=1
                j=j+1
        if max_count<count:
            max_count=count
    print('Length of Maximum Word: ',max_count)
main()