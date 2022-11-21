from GoogleNews import GoogleNews

def search_news(term):
    googlenews = GoogleNews(period='7d', lang='pt-BR')
    googlenews.get_news(term)

    result = googlenews.results()
    return result