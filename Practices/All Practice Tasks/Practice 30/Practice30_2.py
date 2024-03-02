from random import randint

SIZE = 9

def init(a):
    for i in range(SIZE):
        for j in range(SIZE):
            a[i][j] = randint(1, 9)
    a[0][0] = 1  # always one by definition

def print_2d(a):
    for i in range(SIZE):
        for j in range(SIZE):
            print(a[i][j], end=' ')
        print()

def average_out_8_neighbors(a):
    for i in range(1, SIZE - 1):
        for j in range(1, SIZE - 1):
            a[i][j] = (a[i-1][j-1] + a[i-1][j] + a[i-1][j+1] + a[i][j-1] + a[i][j+1] + a[i+1][j-1] + a[i+1][j] + a[i+1][j+1]) // 8

def main():
    x = [[0 for j in range(SIZE)] for i in range(SIZE)]
    init(x)
    print_2d(x)
    print("-------------")
    average_out_8_neighbors(x)
    print_2d(x)

main()
