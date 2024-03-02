def main():
    x=input('First Alphabet:  ')
    y=input('Second Alphabet:  ')
    a=ord(x)
    b=ord(y)
   
    print (f'1st Alphabet: {x}    2nd Alphabet: {y}')
    while a<=b:
        print (chr(a))
        a=a+1

    while a>=b:
        print (chr(a))
        a=a-1

main()
        
