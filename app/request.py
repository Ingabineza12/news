
import urllib.request,json
from app import app
from .models import news

News = news.Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config['NEWS_SOURCES_BASE_URL']


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

        sources_object= Sources(id,name,description,url,category,country,language)
        sources_results.append(sources_object)

    return sources_results
