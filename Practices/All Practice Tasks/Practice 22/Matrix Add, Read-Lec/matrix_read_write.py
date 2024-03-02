from os.path import *
def main():
    filename1 = input("Enter file name for reading with extension: ")
    filename2 = input("Enter file name for writing with extension: ")
    if not (isfile(filename1)) or not (isfile(filename2)):
        print('Error, check input file name or check file name in directory')
        return
    file1 = open(filename1, 'r')
    file2 = open(filename2, 'w')
    rows = int(file1.readline())
    columns = int(file1.readline())
    file2.write(str(rows))
    file2.write(str(columns)+'\n')
    for i in range(rows):
        for j in range(columns):
            value = int(file1.readline())
            print(value, end=' ')
            file2.write(str(value)+' ')
        print()
        file2.write('\n')
    file1.close()
    file2.close()

main()
