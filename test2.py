__author__ = 'andriy'
import unittest
from selenium import webdriver
from home2 import HomePage
from result2 import ResultPage

class TestPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.google.com")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()


    def test_word_is_within_page(self):
        home = HomePage(self.driver)
        home.inputKeyword('python v.3.5')
        result = home.clickSearch()
        #result = ResultPage(self.driver) #there is no neccessety to write this row, because in previous row we init ResultPage
        result.clickGoogleSearchResult(5)
        pageText = result.getTextFromPage() 
        assert 'release' in pageText

if __name__ == '__main__':
    unittest.main(verbosity=2)