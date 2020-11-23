import urllib.request,json
from .models import Sources,Articles
from datetime import datetime

api_key=None
base_url=None
articles_url=None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key=app.config['NEWS_API_KEY']
    base_url=app.config['NEWS_SOURCES_BASE_URL']
    articles_url=app.config['ARTICLES_BASE_URL']

def get_sources(category):
    '''
    function that gets the jsn response
    '''
    get_sources_url=base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data=url.read()
        get_sources_response=json.loads(get_sources_data)
        sources_results=None
        if get_sources_response['sources']:
            sources_results_list=get_sources_response['sources']
            sources_results=process_sources(sources_results_list)
    return sources_results

def process_sources(sources_list):
    '''
    function that process the news sources results
    '''

    sources_results=[]

    for source_item in sources_list:
        id=source_item.get('id')
        name=source_item.get('name')
        description = source_item.get('description')
        url=source_item.get('url')
        category=source_item.get('category')
        language=source_item.get('language')
        country=source_item.get('country')

        sources_object=Sources(id,name,description,url,category,country,language)
        sources_results.append(sources_object)
    return sources_results



def get_articles(id):
    '''
    function to return a list
    '''
    get_articles_url=articles_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url)as url:
        articles_results=json.loads(url.read())
        articles_object=None
        if articles_results['articles']:
            articles_object=process_articles(articles_results['articles'])
    return articles_object

def process_articles(articles_list):
    '''
    function to list all articles
    '''
    articles_object=[]
    for articles_item in articles_list:

        id=articles_item.get('id')

        author=articles_item.get('author ')
        title= articles_item.get('title')

        description = articles_item.get('description ')
        url=articles_item.get('url')

        image=articles_item.get('urlToImage')
        date=articles_item.get('publishedAt')

        if image:
           articles_result=Articles(id,author,title,description,url,image,date)
           articles_object.append(articles_result)
    return articles_object
