from random import *
def main():
	#In question input required, however, here I have used random funciton, hope you are able to take input
	x = randint(1, 5)
	y = randint(1, 5)
	print (f'X: {x}\t\tY: {y}\n')
	result = x * x * x - y * y * y - 3 * x * x * y + 3 * x * y * y - y * y * y
	print (f'Result: {result}')
main()