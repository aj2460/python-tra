birthdays={'Alice':'Apr 1','Bob':'Dec 12'}

while True:
	print('Enter a name: (blank to quit)')
	name=input()
	if name=='':
		break
	if name in birthdays:
		print(birthdays[name] + ' is the birthday of '+ name)
	else:
		print('I do not have birthday information for '+ name)
		pint('What is their birthdat? ')
		bday=input()
		birthday[name]=bday
		print('Birthday database updated')

