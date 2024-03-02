from random import *
def main():
	#In question input required, however, here I have used random funciton, hope you are able to take input
	radius = randint(1, 5)
	print (f'Radius: {radius}')
	area = 4 / 3 * 22 / 7 * radius * radius * radius
	print (f'Area: {area}')
	
main()
