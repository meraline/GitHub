import requests
from bs4 import BeautifulSoup
import pandas as pd
  
#req = requests.get('https://parsinger.ru/table/1/index.html')  
#src=req.text 
#print(src)  
 
 
#with open("index.html", "w") as file:
#  file.write(src) 
  
with open("index.html") as file:
	src = file.read() 

soup = BeautifulSoup(src, "lxml")

#print(soup)

th = [x.text for x in soup.find_all('th')]
print(th)

td = [float(x.text) for x in soup.find_all('td')]
#print(td)
res = []
n=0
for x in td[:n]:
	res.append(x)
	#n+=15
	print(res)

#print(f'td:nth-child({th.split()[0]})')

#data = pd.read_html("index.html", header=0)
#df = data[0]
#df['column']: df['column'].sum()
#print(df)

