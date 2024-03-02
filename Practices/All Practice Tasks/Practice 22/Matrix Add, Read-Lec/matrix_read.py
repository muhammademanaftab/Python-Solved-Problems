from os.path import *
def main():
	filename = input("Enter file name with extension: ")
	if not (isfile(filename)):
		print('Error, check input file name or check file name in directory')
		return
	file = open(filename, "r")
	rows = int(file.readline())
	columns = int(file.readline())
	for i in range(rows):
		for j in range(columns):
			value = int(file.readline())
			print(value, end=' ')
		print()
	file.close()

main()