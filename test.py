__author__ = 'andriy'
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from ddt import ddt, data

from google_page import HomePage
from google_result import ResultPage
#from helper import HelpPage
#from base import BasePage

@ddt
class TestPage(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.google.com")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.close()
    
    @data(1,2,3,4,5)
    def test_word_is_within_page(self, row_number):
        home = HomePage(self.driver, self.wait)
        home.inputKeyword('python v.3.5')
        result = home.clickSearch()
        RowNumberLocator = result.getRowNumberLocator(row_number)
        result.clickGoogleSearchResult(RowNumberLocator)
        searchResultText = result.getTextFromSearchResult(ResultPage.GoogleSearchResult) 
        assert 'release' in searchResultText

if __name__ == '__main__':
    unittest.main(verbosity=2)