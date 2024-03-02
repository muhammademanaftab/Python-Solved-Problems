from random import *

def main():
    a = randint(0, 2)
    b = randint(0, 2)
    c = randint(0, 2)
    d = randint(0, 2)
    e = randint(0, 2)
    print (f'{a}  {b}  {c}  {d}  {e}');
    if (a == b):	print (f'First and second are same');
    if (a == c):	print (f'First and third are same');
    if (a == d):	print (f'First and fourth are same');
    if (a == e):	print (f'First and fifth are same');
    if (b == c):	print (f'Second and third are same');
    if (b == d):	print (f'Second and fourth are same');
    if (b == e):	print (f'Second and fifth are same');
    if (c == d):	print (f'Third and fourth are same');
    if (c == e):	print (f'Third and fifth are same');
    if (d == e):	print (f'Fourth and fifth are same');
main()