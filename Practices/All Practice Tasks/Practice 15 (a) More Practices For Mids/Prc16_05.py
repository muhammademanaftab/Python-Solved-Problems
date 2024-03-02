def main():
    i=2
    x=int(input('Integer: '))
    while x>=i:
        if x%i==0:
            print (f'{x} is divisible by {i}')
        i=i+1
main()
