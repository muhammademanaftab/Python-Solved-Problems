from random import *
def main():
    l=1    
    while l<=10:
        l=l+1
        x=randint (65,90)
        y=chr(x)
        print (f'Alphabet is:  ',y)
        if y=='A'or y=='E' or y=='I' or y=='O' or y=='U':
            print ('Alphabet is Vowel')
        else:
             print ('Alphabet is consonant')
             
main()     
