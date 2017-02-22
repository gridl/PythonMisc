import builtwith
import whois
import urllib2
import re
#print(builtwith.parse('http://www.pythonanywhere.com'))
#print(whois.whois('http:://www.pythonanywhere.com'))

def download(url, user_agent= 'wswp', num_retries = 2):
    print('Downloading ', url)
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print('Download error: ', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                #recursively retry 5xx http errors
                return download(url, num_retries-1)
    return html

def get_links(html):
    """Return a list of links from html
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

#sitemap crawler

def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)


def link_crawler(seed_url, link_regex):
    crawl_queue = [seed_url]
    # keep track which URLs ahve seen before
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            # check if link matches expected regex
            if re.match(link_regex, link):
                # form absolute link
                link = urlparse.urljoin(seed_url, link)
                # check if have already seen this link
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

if __name__ == '__main__':
    #download('http://example.webscraping.com')
    #crawl_sitemap('http://example.webscraping.com/sitemap.xml')
    link_crawler('http://example.webscraping.com', 'example.webscraping.com/(index|view)/')