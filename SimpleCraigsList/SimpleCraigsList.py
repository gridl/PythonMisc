from bs4 import BeautifulSoup
import requests
import logging
import colorlog

site = 'http://portland.craigslist.org/search/muc?query=guitar'
html = 'SimpleCraigsList/craigs.html'
logger = colorlog.getLogger()


def fetch_search_results(query = None):
    resp = requests.get(site,timeout=3)
    resp.raise_for_status()
    file = open("craigs.html", "w")
    file.write(resp.text)
    file.close()
    #return resp.content,resp.encoding

def parse_source(html, encoding='utf-8'):
    soup = BeautifulSoup(open("craigs.html"),"lxml")
    logger.info('Printing Soup')
    #print(soup.prettify())
    logger.info("Finding rows")
    rows = soup.find('div', class_ ='content').find_all('p', 'row')
    print(rows)
    for row in rows:
        print(row)
    #print(soup.prettify())
    logger.info("FInding titles and links")
    for post in soup.find_all('a', class_='result-title hdrlnk'):
        print(post.string,'http://portland.craigslist.org/'+post['href'])



if __name__ == '__main__':
    logger.setLevel(colorlog.colorlog.logging.INFO)
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter())
    logger.addHandler(handler)

    #fetch_search_results()
    parse_source(html)



