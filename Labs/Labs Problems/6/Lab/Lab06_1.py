def main():
    n = 1
    while n <= 99:
        print (f'[{n}', end='')
        if n >=10:
            f = n // 10     # first digit of n
            s = n % 10      # second digit of n
            sum = f + s
            print (f' {sum}', end='')
            if sum >= 10:
                f = sum // 10     # first digit of n
                s = sum % 10      # second digit of n
                sum = f + s
                print (f' {sum}', end='')
        print (']', end='')
        n = n + 1
    print()
main()
