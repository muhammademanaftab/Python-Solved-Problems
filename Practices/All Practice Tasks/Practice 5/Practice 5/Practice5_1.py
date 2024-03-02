from random import *
def main():
	x1 = randint(-5, 5)
	x2 = randint(-5, 5)
	y1 = randint(-5, 5)
	y2 = randint(-5, 5)
	print (f'X1: {x1}\t\tY1: {y1}\t\tX2: {x2}\t\tY2: {y2}')
	distance = ( ( x2 - x1 ) *  ( x2 - x1 )  +  ( y2 - y1 ) *  ( y2 - y1 ) ) ** 0.5
	print (f'Distance: {distance}')

main()
