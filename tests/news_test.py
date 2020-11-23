import unittest
from models import Sources, Articles
News = news.Sources


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

if __name__ == '__main__':
    unittest.main()
