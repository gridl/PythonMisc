import requests
from bs4 import BeautifulSoup

URL = "http://zero.nike.com/home/geo/whq_news"
response = requests.get(URL)
# #URL = 'http://zero.nike.com/home/news/'
content  = response.content
#
#
# # Initialize the parser

#
# soup = BeautifulSoup(content,"lxml")
# print(soup.prettify())
# samples = soup.find_all("a", "item-title")
# print(samples)



from urllib.request import urlopen

page = urlopen (URL)
# print (page.read ())
soup = BeautifulSoup (page.read (),"lxml")
print(soup.prettify())
print(soup.find('div', attrs= {'class' : 'row-fluid'}))