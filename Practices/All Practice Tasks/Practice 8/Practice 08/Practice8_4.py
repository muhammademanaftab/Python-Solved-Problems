from random import *
def main():
	#In question input required, however, here I have used random funciton, hope you are able to take input
	c = randint(97, 122)	#Capital alphabets have ascii 97 to 122
	position = randint(0, 7)
	mask = 2 ** position
	if (c & mask) == mask:
		print (f'The bit number {position+1} is on in {chr(c)}')
	else:
	    print (f'The bit number {position+1} is off in {chr(c)}')
		
main()