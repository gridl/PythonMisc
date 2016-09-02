import urllib
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from bs4 import BeatifulSoup


base_url = "http://apod.nasa.gov/apod/archivepix.html"
download_directory = "apod_pictures"

to_visit = set((base_url,))
visited = set()

while to_visit:
    #pick a link to visit
    current_page = to_visit.pop()
    print("visiting: ", current_page)
    visited.add(current_page)
    content = urllib.request.urlopen(current_page).read()

    for link in BeautifulSoup(content, "lxml").findAll("a"):
        absolute_link = urljoin(current_page, link["href"])
        if absolute_link not in visited:
            to_visit.add(absolute_link)
        else:
            print("Already visited: ", absolute_link)


    for img in BeautifulSoup(content, "lxml").findAll("img"):
        img_href = urljoin(current_page, img["srd"])
        print("Downloading image", img_href)
        img_name = img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))