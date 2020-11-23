import unittest
from app.models import Articles

class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = Articles('evelyne','news','technology','https://google.com','https://google.com/images','2018-05-12T13:31:03Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.author,'evelyne')
        self.assertEquals(self.new_article.title,'news')
        self.assertEquals(self.new_article.description,'Advanced technology improving life')
        self.assertEquals(self.new_article.url,'https://google.com')
        self.assertEquals(self.new_article.urlToImage,'https://google.com/images')
        self.assertEquals(self.new_article.publishedAt,'2018-05-12T13:31:03Z')
