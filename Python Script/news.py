import requests, bs4





res=requests.get('http://news.google.com')
res.raise_for_status()
news=bs4.BeautifulSoup(res.text)

print(news.text)
'''
newsFile=open('news.txt','wb')
for chunk in res.iter_content(100000):
	newsFile.write(chunk)

newsFile.close()
print('Done')

f=open('news.html')
soup=bs4.BeautifulSoup(f)
print(type(soup))
'''