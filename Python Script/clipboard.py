import pyperclip

#pyperclip.copy('hello world')
#print(pyperclip.paste())

text=pyperclip.paste()
#print(text)
text=text.split('\n')
'''t=[]
for i in text:
	t.append('* '+i)
text='\n'.join(t)	
#pyperclip.copy(text)
'''

for i in range(len(text)):
	text[i]='* '+text[i]
text='\n'.join(text)


print(text)
pyperclip.copy(text)




