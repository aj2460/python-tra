#spam. setdefault(' color' , ' white' )
allGuests={'Alice':{'apples':5,'pretzels':12},
			'Bob':{'ham sandwiches':3,'apples':2},
			'Carol':{'cups':3,'apple pies':1}}

def totalBrought(guest,item):
	numBrought=0
	for k,v in guest.items():
		numBrought+=v.get(item,0)
	return numBrought


if __name__ == '__main__':
	#print (list(allGuests.values()))
	items=[]
	for value in allGuests.values():
		#print(value)
		for item in value.keys():
			#print (item)
			if item not in items:
				items.append(item)

	#print (items)
	print('Number of things being brought:')
	for i in items:
		print(i, ' - ',str(totalBrought(allGuests,i)))