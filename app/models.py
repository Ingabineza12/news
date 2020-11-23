class Sources:
    '''
    Sources class that defines source objects
    '''
    def __init__(self,id,name,description,url,category,language,country):
        '''
        Function that initiates the sources class
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class Articles:
    '''
    Sources class that defines source objects
    '''
    def __init__(self,id,author,title,description,url,urlToImage,publishedAt,content):
        '''
        Function that initiates the sources class
        '''
        self.id = id

        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
