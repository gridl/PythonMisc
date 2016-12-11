import smtplib
import time
import colorlog
import conf
import requests
import schedule
from bs4 import BeautifulSoup

site = 'http://portland.craigslist.org/search/muc?query=guitar'
html = 'SimpleCraigsList/craigs.html'
logger = colorlog.getLogger()
allposts = []

def fetch_search_results(query=None):
    logger.info('Fetching search results')
    resp = requests.get(site, timeout=3)
    resp.raise_for_status()
    file = open("craigs.html", "w")
    file.write(resp.text)
    file.close()
    # return resp.content,resp.encoding


def parse_source():
    logger.info("Parsing rows from HTML")
    soup = BeautifulSoup(open("craigs.html"), "lxml")
    # logger.info('Printing Soup')
    # print(soup.prettify())
    # logger.info("Finding rows")
    #print(soup.prettify())
    #logger.info("Finding titles and links")
    for post in soup.find_all('a', class_='result-title hdrlnk'):
        posts = post.string, 'http://portland.craigslist.org/' + post['href']
        allposts.append(str(posts))
    return '\n'.join(allposts).encode('utf-8')


def by_schedule():
    logger.info("Reading schedule")
    schedule.every().day.at("13:00").do(send_mail)
    while True:
        schedule.run_pending()
        time.sleep(1)


def send_mail():
    logger.info("Connecting to mail server")
    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.ehlo()
    server.starttls()
    server.login(conf.send, conf.key)
    msg = parse_source()
    server.sendmail(conf.send, conf.rec, msg)
    logger.info("Sending mail")
    server.quit()




if __name__ == '__main__':
    logger.setLevel(colorlog.colorlog.logging.INFO)
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter())
    logger.addHandler(handler)
    fetch_search_results()
    parse_source()
    by_schedule()

