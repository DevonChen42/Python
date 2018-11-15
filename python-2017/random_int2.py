# save this file as random_int.py
from random import randint
def randlist(r,usedlist,done):
	alpha = ["a","b","c","d","e","f"]
	usedlist[r] = 1
	c = alpha[r]
	sum = 0
	for i in range(len(usedlist)):
		sum = sum + usedlist[i]
	# print (sum)
	return c, usedlist
	
def main():
	used = [0,0,0,0,0,0]
	done = True
	while True:
		r = randint(0,5)
		c = randlist(r,used,done)
		print (used)
		#print(c,end='')
main()
