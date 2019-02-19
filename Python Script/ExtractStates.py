import re
f=open('states.txt','r')
li=[]
#stateReges=re.compile(r'<p>([\w\s-]+|[\w\s]+\([\w\s]+\))</p>')
stateReges=re.compile(r'([A-Z]\w+[\s\&\;\'\-()\w\s]*)')
text=f.read()
mo=stateReges.findall(text)
	#if mo:
#print(mo)
		#li.append(mo)
	#print(line)
	#print('-'*20)
fwrite=open('StateDict.txt','w')
fwrite.write('{')
x=1
for i in range(len(mo)):
	
	if (i+1)%3==0:
		print()
		#print(x,end=' ')
		#x+=1
		continue
	fwrite.write("'")
	#print(str(mo[i]).ljust(35) , end=' ')
	fwrite.write(str(mo[i]))
	fwrite.write("'")
	if x%2==1:
		fwrite.write(":")
	else:
		fwrite.write(",")
	x+=1

fwrite.write('}')		
fwrite.close()	




