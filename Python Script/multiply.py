import sys

def table(n):
	for i in range(1,13):
		print('{0:2} X {1:2} = {2:^}'.format(n,i,i*int(n)))




def main():
	for x in range(1,len(sys.argv)):
		print('Table of {}'.format(sys.argv[x]))
		print('{}'.format('-'*12))
		table(sys.argv[x])
		print('{}'.format('='*12))
		


if __name__=='__main__':
	main()
