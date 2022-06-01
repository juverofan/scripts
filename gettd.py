import sys
#import urllib2
from urllib.request import Request, urlopen
import weasyprint
from bs4 import BeautifulSoup
import os


url = ""
if len(sys.argv) > 1:
	url = str(sys.argv[1])

page = 1000
if len(sys.argv) > 2:
	page = str(sys.argv[2])
print(str(sys.argv))


filename = url.split("threads/")[1].split("/")[0]
baseurl = url
orw = open(filename+".html","w+", encoding="utf-8")
t = 1
strT = ""
lastStr = ""
curStr = ""
if page != 1000:
	url = baseurl+"page-"+str(page) 
	print(url)
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	html_doc = urlopen(req).read()

	soup = BeautifulSoup(html_doc, 'html.parser')
	author = []
	for x in soup.find_all("div", {"class": "message-avatar-wrapper"}): 
		author.append(x)
	z = 0
	for x in soup.find_all("div", {"class": "bbWrapper"}): 
		
		#curStr += str(x)+"<br>"
		#if lastStr != curStr:
		if author[z] == author[0]:
			print(x)
			strT += str(x)+"<br>"
		z += 1
else:
	author = []
	while t < 1000:
		lastStr = curStr
		curStr = ""
		try:
			if t > 1:
				url = baseurl+"page-"+str(t) 
			print(url)
			req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
			html_doc = urlopen(req).read()

			soup = BeautifulSoup(html_doc, 'html.parser')
			author1 = []
			for x in soup.find_all("div", {"class": "message-avatar-wrapper"}): 
				#print(x)
				author.append(x)
				author1.append(x)

			print(str(len(author)) + " | " + str(len(author1)) )
			z = 0
			for x in soup.find_all("div", {"class": "bbWrapper"}): 
				print(str(z))
				if author1[z] == author[0]:
					curStr += str(x)+"<br>"
				#	print(str(z))
				#	print(str(len(curStr)))
				#print(str(z))
				z += 1
			print("abc")
			print("Total:"+str(len(curStr)))
			print(str(len(lastStr)))

			if lastStr != curStr:
				print(curStr)
				strT += curStr
			else:
				print("day")
				t = 1001
			t += 1
		except:
			print("o day")
			t = 1001

orw.write(str(strT))
orw.close()
pdf = weasyprint.HTML(filename+".html").write_pdf()
open(filename+'.pdf', 'wb').write(pdf)
if os.path.isfile(filename+'.pdf'):
	os.system("del "+filename+".html")