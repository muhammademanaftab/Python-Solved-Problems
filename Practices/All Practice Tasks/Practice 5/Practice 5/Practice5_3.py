from random import *
def main():
	#In question input required, however, here I have used random funciton, hope you are able to take input
	vi = randint(1, 10)
	a = randint(1, 5)
	t = randint(1, 5)
	print (f'initial velocity: {vi}')
	print (f'acceleration: {a}')
	print (f'time: {t}')
	vf = vi + a * t ;
	print (f'Final Velocity: {vf}')
	
	d = randint(1, 5)
	print (f'----------------------------------\n')
	print (f'initial velocity: {vi}')
	print (f'acceleration: {a}')
	print (f'time: {t}')
	vf_square = vi * vi + 2 * a * d
	print (f'Final Velocity Square: {vf_square}')
	
	print (f'----------------------------------\n')
	print (f'initial velocity: {vi}')
	print (f'acceleration: {a}')
	print (f'time: {t}')
	d = vi * t + 1 / 2.0 * a * t * t
	print (f'Distance: {d}')

main()
