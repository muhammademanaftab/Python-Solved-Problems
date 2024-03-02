def next_vowel(a):
    c=ord(a)
    if c<69 or c<101  :
        print ('e')
    elif c <73 or c<105:
        print ('i')
    elif c<79 or c<11:
        print ('o')
    elif c < 85 or c<117:
        print ('u')
    else:
        print('a')
a=input('Character:  ')
next_vowel(a)

    
