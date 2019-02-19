import sys
def readFile(filename):
	f=open(filename,'rU')
	for line in f:
		print (line,end='')

	#lines=f.readlines() #read to lines variable as a list with each line a s a tuple
	#print(lines)

	#text=f.read()  #read the file to text varial asa string
	#print(text)
	f.close()

def main():
	readFile(sys.argv[1])


if __name__=='__main__':
	main()
