tableData = [[' apples' , ' oranges' , ' cherries' , ' banana' ] ,
[' Alice' , ' Bob' , ' Carol' , ' David' ] ,
[' dogs' , ' cats' , ' moose' , ' goose' ] ]

colWidths=[0]*len(tableData)
for i in range(len(tableData)):
	#print(item)
	for j in tableData[i]:
		if len(j)>colWidths[i]:
			colWidths[i]=len(j)


print(colWidths)


for i in tableData:
	print(i)

print(tableData[1][2])

for i in range(4):
	for k in range(3):
		print(tableData[k][i].rjust(colWidths[k]),end='')
	print()