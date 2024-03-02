from os.path import *
def main():
    if not (isfile('marks.txt')):
        print('Error, check input file name or check file name in directory')
        return
    file = open('marks.txt', 'r')
    count = int(file.readline())        #read number of classes
    for i in range(count):
        total = 0
        n = int(file.readline())        #read number of students
        for j in range(n):
            marks = int(file.readline())    #read marks of each student
            print (marks, end = ' ')
            total += marks
        print('\tAverage: ', total/n)
    file.close()

main()
