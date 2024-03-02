def main():
    f1=open('paragraph.txt','r')
    sen=f1.readline()
    w_d=0
    for i in range (26):
        count=0        
        a=chr(65+i) 
        b=chr (ord(a)+32)          
        for i in range (len(sen)):
            w=''
            if i==0:
                w+=sen[i]
                if a==w:
                    count+=1
                    w_d+=1
            elif sen[i]==' ':
                w+=sen[i+1]
                if a==w or b==w:
                    count+=1
                    w_d+=1
        if count >0:            
            print(f'Words Start From {a} are: ', count)
    print('Total Words count by adding word count of individual alphabets:',w_d)
main()                   
               


