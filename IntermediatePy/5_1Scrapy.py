# from the archive, follow each link and find the image in that linked page and downlaod the image.

# Concepts

# downloading stuff

from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()

content = http.request("GET","http://apod.nasa.gov/apod/archivepix.html")
# print(content.data)
links =  BeautifulSoup(content.data,"lxml").findAll("a")
for link in links:
    # print(link)
    print(link.get('href'))


    content = url