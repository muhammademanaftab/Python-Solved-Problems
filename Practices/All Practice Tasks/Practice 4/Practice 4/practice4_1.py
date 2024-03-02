def main():
    a = int ( input ('Enter A: '))
    b = int ( input ('Enter B: '))
    c = int ( input ('Enter C: '))
    if a == 0:
        print (f'Equation is linear having only one root:  {-c/b}')
        return
    disc = b * b - 4 * a * c
    if disc < 0:
        print (f'Roots are imaginary')
        return
    disc = disc ** 0.5
    d = 2 * a
    x1 = ( -b + disc ) / d
    x2 = ( -b - disc ) / d
    print ('X1:', x1)
    print ('X2:', x2)

main()
