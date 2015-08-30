def cheese_potatoes(N):
	if N%3==0 and N%5==0:
		print 'cheese and potatoes'
	elif N%5==0:
		print 'cheese'
	elif N%3==0:
		print 'potatoes'
	else:
		print N

def user_input():
	n = raw_input("What is your number?  ")
	n = int(n)	
	cheese_potatoes(n)

def main():
	user_input()

main()
