import feedparser





feeds = feedparser.parse('https://news.google.ca/news/feeds?pz=1&cf=all&ned=en&hl=ca&q=software+engineering&output=rss') 

print(type(feeds.entries))

for i in range(10):
    print(feeds.entries[i].link)
    print(feeds.entries[i].title)
