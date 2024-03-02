def main():
    x = int(input('Number: '))
    factorial=x
    i = 1
    while i < x:        
        factorial = factorial * i        
        i = i + 1
    print(factorial)

main()

