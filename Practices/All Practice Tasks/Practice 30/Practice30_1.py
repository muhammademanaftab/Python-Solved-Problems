from random import randint
SIZE = 9
def init(a):
    for i in range(SIZE):
        for j in range(SIZE):
            a[i][j] = randint(0, 1)
    a[0][0] = 1  # always one by definition

def print_2d(a):
    for i in range(SIZE):
        for j in range(SIZE):
            print(a[i][j], end=' ')
        print()

def print_path(a):
    i = 0
    j = 0
    while True:
        print(f"{i}, {j}", end=' ')
        if i != SIZE - 1 or j != SIZE - 1:
            print("-", end=' ')
        if j + 1 < SIZE and a[i][j + 1] == 1:
            j += 1
        elif i + 1 < SIZE and a[i + 1][j] == 1:
            i += 1
        else:
            break
    if i != SIZE - 1 or j != SIZE - 1:
        print("path blocked")
    else:
        print()

def main():
    x = [[0 for j in range(SIZE)] for i in range(SIZE)]
    init(x)
    print_2d(x)
    print_path(x)

main()
