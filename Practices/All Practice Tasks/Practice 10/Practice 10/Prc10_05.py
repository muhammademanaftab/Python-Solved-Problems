def main():
    x=int(input('Enter number;  '))
    y=int(input('Enter number;  '))
    a=int(input('Enter number;  '))
    b=int(input('Enter number;  '))
    c=int(input('Enter number;  '))
    if x>y and x>a and x>b and x>c:
        print (x)
    if y>x and y>a and y>b and y>c:
        print(y)
    if a>x and a>y and a>b and a>c:
        print(a)
    if b>x and b>y and b>a and b>c:
        print(b)
    if b>x and b>a and b>y and c>b:
        print(c)
main()        
        
        
    
