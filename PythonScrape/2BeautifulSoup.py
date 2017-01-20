import requests
from bs4 import BeautifulSoup

response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
content  = response.content
print(content)


# Initialize the parser
parser = BeautifulSoup(content, 'html.parser')

# BS allows accessing branches by using tag types as attributes
body = parser.body

# Get the p tag from the body
p = body.p
print(p.text)

# Get the title
head = parser.head
title_text = head.title
print(title_text.text)


#using find_all

# get a list of all occurrences of the body tag in the element
body = parser.find_all("body")

# get the paragraph tag
p = body[0].find_all("p")
print(p)
# get the text
print(p[0].text)

# get the title tag
head = parser.find_all("head")
title = head[0].find_all("title")
title_text = title[0].text
print(title_text)
