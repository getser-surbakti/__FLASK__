from flask import Flask
import feedparser

app = Flask(__name__)
BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route("/getnews")
def get_news():
    feed = feedparser.parse(BBC_FEED)
    articles = feed['entries'][:5]  # Get the first 5 articles
    articles_html = ""
    for article in articles:
        articles_html += """<b>{0}</b> <br/>
                            <i>{1}</i> <br/>
                            <p>{2}</p> <br/><br/>""".format(article.get("title"), article.get("published"), article.get("summary"))
    return """<html>
 <body>
 <h1> BBC Headlines </h1>
 {0}
 </body>
</html>""".format(articles_html)

if __name__ == '__main__':
    app.run(debug=True)
