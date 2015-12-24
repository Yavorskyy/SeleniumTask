from result2 import ResultPage
from loc import HomeLoc

class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
    
    def inputKeyword(self, param):
        self.driver.find_element_by_xpath(HomeLoc.GoogleSearchField).send_keys(param)

    def clickSearch(self):
        self.driver.find_element_by_xpath(HomeLoc.GoogleSearchButton).click()
        return ResultPage(self.driver)