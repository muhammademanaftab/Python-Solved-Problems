def next_vowel(c):
    a=ord (c)
    i=65
    if c=='A' or c=='a' or c=='E' or c=='e':
        while i<(4+a):
            i=i+1
        print (chr(i))
    if c=='I' or c=='i' or c=='o' or c=='O' :
        while i<(6+a):
            i=i+1
        print(chr(i))
    if c=='U' or c=='u':
        print ('A')
c=input('Vowel:  ')
next_vowel(c)
        
