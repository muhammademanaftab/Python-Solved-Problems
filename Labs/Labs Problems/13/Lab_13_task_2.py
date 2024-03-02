def main():
    f1=open('paragraph.txt','r')
    sen=f1.readline()
    w_d=0
    for i in range (26):
        count=0        
        a=chr(65+i) 
        b=chr (ord(a)+32)          
        for i in range (len(sen)):
            if sen[i]==a or sen[i]==b:
                count+=1
                w_d+=1
        if count >0:            
            print(f'Letter {a} Appears {count} times')
    print('Total Alphabets in the Paragraph:',w_d)
    print('Total Characters in the Paragraph:',len(sen))

main()  