import feedparser

def feeds(industryVertical):
    
    myFeeds = list()
    industryVertical = industryVertical.replace(' ','+')
    try:
        feeds = feedparser.parse('https://news.google.ca/news/feeds?pz=1&cf=all&ned=en&hl=ca&q='+industryVertical+'&output=rss')
        for i in range(25):
            myFeeds.append(feeds.entries[i])
        return myFeeds

    except Exception as e:
        return myFeeds
