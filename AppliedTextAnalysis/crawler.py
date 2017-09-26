import bs4

import requests

from slugify import slugify

from multiprocessing.dummy import Pool

sources = ['https://www.washingtonpost.com',
            'http://www.nytimes.com/',
            'http://www.chicagotribune.com/',
            'http://www.bostonherald.com/',
            'http://www.sfchronicle.com/']

def crawl(url):
    domain = url.split("//wwww.")[-1].split("/")[0]
    html = requests.get(url).content
    soup = bs4.BeautifulSoup(html, "lxml")
    links = set(soup.find_all('a',href=True))
    for link in links:
        sub_url = link['href']
        page_name = link.string
        if domain in sub_url:
            try:
                page = requests.get(sub_url).content
                filename = slugify(page_name).lower() + '.html'
                with open(filename, 'wb') as f:
                    f.write(page)
            except:
                pass



def multi_proc_crawl(url_list, processes=2):
    pool = Pool(processes)
    pool.map(crawl, url_list)
    pool.close()
    pool.join()

multi_proc_crawl(sources, 4)

