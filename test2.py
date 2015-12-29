__author__ = 'andriy'
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from home2 import HomePage
from result2 import ResultPage
from loc import HomeLocator

class TestPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.google.com")
        self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(HomeLocator.GoogleSearchField))

    #def tearDown(self):
    #    self.driver.close()


    def test_word_is_within_page1(self):
        home = HomePage(self.driver)
        home.inputKeyword('python v.3.5')
        result = home.clickSearch()
        #result = ResultPage(self.driver) #there is no neccessety to write this row, because in previous row we init ResultPage
        result.clickGoogleSearchResult(1)
        pageText = result.getTextFromPage() 
        assert 'release' in pageText

    def test_word_is_within_page2(self):
        home = HomePage(self.driver)
        home.inputKeyword('python v.3.5')
        result = home.clickSearch()
        #result = ResultPage(self.driver) #there is no neccessety to write this row, because in previous row we init ResultPage
        result.clickGoogleSearchResult(2)
        pageText = result.getTextFromPage() 
        assert 'release' in pageText

    def test_word_is_within_page3(self):
        home = HomePage(self.driver)
        home.inputKeyword('python v.3.5')
        result = home.clickSearch()
        #result = ResultPage(self.driver) #there is no neccessety to write this row, because in previous row we init ResultPage
        result.clickGoogleSearchResult(3)
        pageText = result.getTextFromPage() 
        assert 'release' in pageText

    def test_word_is_within_page4(self):
        home = HomePage(self.driver)
        home.inputKeyword('python v.3.5')
        result = home.clickSearch()
        #result = ResultPage(self.driver) #there is no neccessety to write this row, because in previous row we init ResultPage
        result.clickGoogleSearchResult(4)
        pageText = result.getTextFromPage() 
        assert 'release' in pageText

    def test_word_is_within_page5(self):
        home = HomePage(self.driver)
        home.inputKeyword('python v.3.5')
        result = home.clickSearch()
        #result = ResultPage(self.driver) #there is no neccessety to write this row, because in previous row we init ResultPage
        result.clickGoogleSearchResult(5)
        pageText = result.getTextFromPage() 
        assert 'release' in pageText

if __name__ == '__main__':
    unittest.main(verbosity=2)