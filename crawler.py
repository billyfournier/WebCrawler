# import the urlopen function from the urllib2 module
from urllib2 import urlopen
# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
import pprint
# choose the url to crawl
url = 'http://www.codingdojo.com'
# get the result back with the BeautifulSoup crawler
soup = BeautifulSoup(urlopen(url), "html.parser")
# print soup # print soup to see the result!!

# print type(soup)
# for ele in soup:
#     if "<a" in ele:
#         print ele
# your code here to find all the links from the result
# and complete the challenges below
titleTag = soup.html.head.title

# print '\n\n'
# print titleTag
# print titleTag.string
# setHREF = set()
# for a in soup.findAll('a', href=True):
#     setHREF.add(a['href'])
#
# lst = list(setHREF)     #converts from set to list
# lst = [x.encode('utf8') for x in lst]   #converts from unicode --> utf8
# for x in sorted(lst): print(x)
crawler = {}
for a in soup.findAll('a', href=True):
    if a['href'] not in crawler:
        print "adding entry into crawler"
        crawler[a['href']] = 1
    else:
        crawler[a['href']] += 1
for entry in crawler.items():
    print entry
