from flask import Flask
from flask import render_template
from flask import request #global context to access information about the latest request
import feedparser
app  = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}


@app.route("/")
def get_news():
    query = request.args.get("publication")
    # get arguments that our uses passes along as part of a request are automatically available in request.args from \
    #     which we can key value paris as we would in a python dictionary
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html",articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5006,debug=True)