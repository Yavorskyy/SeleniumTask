from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from base import BasePage

class ResultPage(BasePage):
    GoogleSearchRow = (By.XPATH, ".//*[@id='rso']/div/div[{}]/div/h3/a")
    GoogleSearchResult = (By.TAG_NAME, "body")


    def getRowNumberLocator(self, row_number):
        RowNumberLocator = list(ResultPage.GoogleSearchRow) #locator with result rows on google page(from GoogleSearchResults class)
        RowNumberLocator[1] = RowNumberLocator[1].format(row_number) #enter needed number of row in locator xpath
        return tuple(RowNumberLocator)

    def clickGoogleSearchResult(self, RowNumberLocator):
    	self.wait.until(EC.presence_of_element_located(RowNumberLocator))  	
        self.driver.find_element(*RowNumberLocator).click() #click needed result row