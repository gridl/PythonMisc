# from the archive, follow each link and find the image in that linked page and downlaod the image.

# Concepts

# downloading stuff\
import urllib

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from bs4 import BeatifulSoup

base_url = "http://apod.nasa.gov/apod/archivepix.html"
content = urllib.request.urlopen(base_url).read()

for link in BeautifulSoup(content, "lxml").findAll("a"):
    print("FOllowing link: ", link)
    href = urljoin(base_url, link["href"])

    content = urllib.request.urlopen(href).read()
    for img in BeautifulSoup(content, "lxml").findAll("img"):
        img_href = urljoin(href,img["src"])
        print("Downloading images ", img_href)
        img_name = img_href.split("/")[-1]
        download_directory = "~/Projects/PythonMisc"
        urllib.request.urlretrieve(img_href, os.path.join(download_directory + "/" + img_name))
