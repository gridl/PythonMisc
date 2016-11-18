import requests
from bs4 import BeautifulSoup

url = 'http://www.blog.pythonlibrary.org/'
url2 = 'https://www.twitter.com/ingvay7'

# first example
def get_articles():
    # Get the articles from the front page of the blog
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.findAll('h1')

    articles = {i.a['href']: i.text.strip() for i in pages if i.a}
    for article in articles:
        s = '{title}: {url}'.format(title=articles[article],url=article)
        print(s)

# second example
def twitter():
    req = requests.get(url2)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    tweets = soup.findAll('li','js-stream-item')
    for item in range(len(soup.find_all('p', 'TweetTextSize'))):
        tweet_text = tweets[item].get_text()
        print(tweet_text)
        dt = tweets[item].find('a','tweet-timestamp')
        print('This was tweeted on ' + str(dt))


if __name__ == '__main__':
    #articles = get_articles()
    twitter()



