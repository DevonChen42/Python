#save this file as random int.py
from random import randint
def ranint():
	r = randint(65,91)
	return r
	
def main():
	for r in range (100000):
		ri = ranint()
		print (ri,end="")
# its 16 spaces, thats how you get it to print diagonally
main()

