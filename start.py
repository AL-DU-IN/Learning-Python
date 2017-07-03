import sys
def check():
	x=0
	l=[]
	while (x<4):
		try:
			a=raw_input("Enter a number\n")
			y=int(a)
			l.append(y)
		except ValueError:
			x+=1
	raise TypeError(" Tries exceeded")
	print(l)
check()