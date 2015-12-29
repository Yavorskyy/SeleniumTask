from result2 import ResultPage
from locator import HomeLocator

class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
    
    def inputKeyword(self, param):
        self.driver.find_element(*HomeLocator.GoogleSearchField).send_keys(param)
        #return HomePage(self.driver)

    def clickSearch(self):
        self.driver.find_element(*HomeLocator.GoogleSearchButton).click()
        return ResultPage(self.driver)




