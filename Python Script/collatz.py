#Collatz Sequence

def collatz(number):
	if number%2==0:
		return number//2
	else:
		return number *3 +1

while True:
	try:
		print('Enter number : ')
		num=int(input())
		break
	except ValueError:
		print('Enter a valid number.')
		continue
while True:
	num=collatz(num)
	print(num)
	if num==1:
		break