import os
#os.mkdir('backup2')
for folderName,subfolders,filenames in os.walk(r'e:\test'):
	print('The current folder is '+folderName)

	for subfolder in subfolders:
		print('Subfolder of ' + folderName + ' : '+subfolder)
	for filename in filenames:
		print ('File Inside ' + folderName + ' : ' +filename)
