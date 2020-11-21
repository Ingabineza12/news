
class Config:
    '''
    General configuration parent class
    '''
    # MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources/{}?api_key={}'
    # NEWS_API_BASE_URL='https://newsapi.org/v2/sources?category=general&apiKey=3530228c891345a787748c97ba00ac2a'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
