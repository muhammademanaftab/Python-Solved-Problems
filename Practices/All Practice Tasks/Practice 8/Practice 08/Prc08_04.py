def main():
    x=str(input('Enter Character:  '))
    a=ord(x)
    y=int(input ('Enter Bit Number:  '))
    b=2**(y-1)
    if a&b==b:
        print(f'The bit number {y} is on in {x}')
    else:
        print (f'The bit number {y} is off in {x}')

main ()
main()
