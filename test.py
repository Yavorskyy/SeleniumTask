__author__ = 'andriy'
import unittest
from selenium import webdriver

from google_page import HomePage
from google_result import ResultPage

class TestPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.google.com")

    def tearDown(self):
        self.driver.close()
    
    def test_word_is_within_page1(self):
        home = HomePage(self.driver)
        home.inputKeyword('python v.3.5')
        result = home.clickSearch()
        RowNumber = result.getRowNumber(1)
        result.clickGoogleSearchResult(RowNumber)
        searchResultText = result.getTextFromSearchResult() 
        assert 'release' in searchResultText
    
    def test_word_is_within_page2(self):
        home = HomePage(self.driver)
        home.inputKeyword('python v.3.5')
        result = home.clickSearch()
        RowNumber = result.getRowNumber(2)
        result.clickGoogleSearchResult(RowNumber)
        searchResultText = result.getTextFromSearchResult() 
        assert 'release' in searchResultText
    
    def test_word_is_within_page3(self):
        home = HomePage(self.driver)
        home.inputKeyword('python v.3.5')
        result = home.clickSearch()
        RowNumber = result.getRowNumber(3)
        result.clickGoogleSearchResult(RowNumber)
        searchResultText = result.getTextFromSearchResult() 
        assert 'release' in searchResultText
    
    def test_word_is_within_page4(self):
        home = HomePage(self.driver)
        home.inputKeyword('python v.3.5')
        result = home.clickSearch()
        RowNumber = result.getRowNumber(4)
        result.clickGoogleSearchResult(RowNumber)
        searchResultText = result.getTextFromSearchResult() 
        assert 'release' in searchResultText
        
    def test_word_is_within_page5(self):
        home = HomePage(self.driver)
        home.inputKeyword('python v.3.5')
        result = home.clickSearch()
        RowNumber = result.getRowNumber(5)
        result.clickGoogleSearchResult(RowNumber)
        searchResultText = result.getTextFromSearchResult() 
        assert 'release' in searchResultText

if __name__ == '__main__':
    unittest.main(verbosity=2)