import unittest
from app.models import Sources, Articles


class NewTest(unittest.TestCase):
    '''
    Test class to test the bahaviour of the New class
    '''

    def setUp(self):
        '''
        set up method that will run before evry test
        '''
        self.new_source=Sources("CNN","CNN News", "Cable News Networks that is a leader in providings news worlwide","cnn.com","general","USA","en")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'CNN')
        self.assertEquals(self.new_source.name,'CNN News')
        self.assertEquals(self.new_source.description,'Cable News Networks that is a leader in providings news worlwide')
        self.assertEquals(self.new_source.url,'cnn.com')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'USA')
        self.assertEquals(self.new_source.language,'en')


class ArticlesTest(unittest.TestCase):
    '''
    class to test the Articles class
    '''
    def setUp(self):
        '''
        method that will run before our test
        '''
        self.new_article=Articles('CNN','Peter Polle', 'The tech scene in Africa is it the next big thing','A look at various tech hubs in Africa','techi.com','techinie.com/7643t94.jpg','2018-04-11T07:57:16Z')

    def tests_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'CNN')
        self.assertEquals(self.new_article.author,'Peter Polle')
        self.assertEquals(self.new_article.title,'The tech scene in Africa is it the next big thing')
        self.assertEquals(self.new_article.description,'A look at various tech hubs in Africa')
        self.assertEquals(self.new_article.url,'techi.com')

        self.assertEquals(self.new_article.image,'techinie.com/7643t94.jpg')
        self.assertEquals(self.new_article.date,'2018-04-11T07:57:16Z')
