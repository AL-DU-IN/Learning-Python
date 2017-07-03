import sys
import math
import itertools
def swap(s):
	a="";
	for x in s:
		a+=x.swapcase()

	return a
def split(s):
	l=s.split(" ")
	print l
	x="!".join(l)
	print(x)
def score(s):
	vowel="AEIOU"
	a,b,m=0,0,0
	l=[]
	for x in range(len(s)):
		if s[x] in vowel:
			a+=len(s)-x
		else:
			b+=len(s)-x
	l.append(a)
	l.append(b)
	return l
def angle(a,b):
	m=math.degrees(math.atan(a/b))
	if(m-math.floor(m)>=0.5):
		return math.ceil(m)
	else:
		return math.floor(m)
def product():
	a=[1,2,3,4]
	b=[2,3]
	c=[a,b]
	print(list(itertools.product(a,b)))
	print(list(itertools.permutations(a)))
def main():
	#x=raw_input("Enter your name\n")
	#float(raw_input("Enter the length of the first side:\n"))
	#b=float(raw_input("Enter the length of the second side:\n"))
	#swap(x)
	#split(x)
	#print(score(x))
	#print(angle(a,b))
	#useless
	product()
main()