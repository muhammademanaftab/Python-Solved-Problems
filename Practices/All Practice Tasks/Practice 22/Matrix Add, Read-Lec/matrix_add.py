from os.path import *
def main():
    filename1 = input("Enter matrix 1 name: ")
    filename2 = input("Enter matrix 2 name: ")
    filename_ans = input("Enter answer matrix name: ")
    if not (isfile(filename1)) or not (isfile(filename2)):
        print('Error, check input file name or check file name in directory')
        return
    file1 = open(filename1, 'r')
    file2 = open(filename2, 'r')
    file_ans = open(filename_ans, 'w')
    rows = int(file1.readline())
    columns = int(file1.readline())
    rows = int(file2.readline())
    columns = int(file2.readline())
    file_ans.write(str(rows)+' ')
    file_ans.write(str(columns)+'\n')
    for i in range(rows):
        for j in range(columns):
            value1 = int(file1.readline())
            value2 = int(file2.readline())
            file_ans.write(str(value1 + value2)+' ')
        print()
        file_ans.write('\n')
    file1.close()
    file2.close()
    file_ans.close()

main()
