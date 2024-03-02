from random import *
def main():
    n = 1
    marks = 0
    while n <= 10:
        n1 = randint(1, 9)
        n2 = randint(1, 9)
        print (f'N1: {n1}\tN2: {n2}')
        sum = int(input('Sum:' ))
        if sum == n1 + n2:  marks = marks + 1;
        else:
            sum = int(input('Wrong, Enter Sum Again:' ))
            if sum == n1 + n2:  marks = marks + 1;
            else:
                sum = int(input('Again Wrong, Last Chance to Enter Sum:' ))
                if sum == n1 + n2:  marks = marks + 1;
        difference = int(input('Difference:' ))
        if difference == n1 - n2:  marks = marks + 1;
        else:
            difference = int(input('Wrong, Enter Difference Again:' ))
            if difference == n1 - n2:  marks = marks + 1;
            else:
                difference = int(input('Again Wrong, Last Chance to Enter Difference:' ))
                if difference == n1 - n2:  marks = marks + 1;
        product = int(input('Product:' ))
        if product == n1 * n2:  marks = marks + 1;
        else:
            product = int(input('Wrong, Enter Product Again:' ))
            if product == n1 * n2:  marks = marks + 1;
            else:
                product = int(input('Again Wrong, Last Chance to Enter Product:' ))
                if product == n1 * n2:  marks = marks + 1;
        n = n + 1
    print('Obtained Marks: ', marks)
main()
