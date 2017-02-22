import urllib.request

url = urllib.request.urlopen('https://www.google.com')
url.geturl()
header = url.info()
header.as_string()


# downloading a file

# url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbView3 er.zip'
# response = urllib.request.urlopen(url)
# data = response.read()
# with open('/path/to /download/','wb') as fobj:
#     fobj.write(data)

#Convert a relative URL to an absolute URL
from urllib.parse import urlparse
result = urlparse('http://duckduckgo.com/?q=python+stubbing&t=canonical&ia=qa')
print(result)
print(result.netloc)
print(result.port)


# submitting a webform

import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'q':'Python'})
url = 'http://duckduckgo.com/html/'
print(data)
full_url = url + '?' + data
response = urllib.request.urlopen(full_url)


# robot parser

import urllib.robotparser
robot = urllib.robotparser.RobotFileParser()
robot.set_url('http://arstechnica.com/robots.txt')
robot.read()
print(robot.can_fetch('*','http://arstechnica.com/'))
