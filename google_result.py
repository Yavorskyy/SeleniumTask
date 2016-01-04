from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPage(object):
    GoogleSearchRow = (By.XPATH, ".//*[@id='rso']/div/div[{}]/div/h3/a")
    GoogleSearchResult = (By.TAG_NAME, "body")

    def __init__(self, driver):
        self.driver = driver

    def getRowNumber(self, row_number):
        RowNumber = list(ResultPage.GoogleSearchRow) #locator with result rows on google page(from GoogleSearchResults class)
        RowNumber[1] = RowNumber[1].format(row_number) #enter needed number of row in locator xpath
        return tuple(RowNumber)

    def clickGoogleSearchResult(self, RowNumber):
    	wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(RowNumber))  	
        self.driver.find_element(*RowNumber).click() #click needed result row


    def getTextFromSearchResult(self):
        data_from_page = self.driver.find_elements(*ResultPage.GoogleSearchResult) # all data within webpage
        text = [comment.text for comment in data_from_page] # all this data put into the list
        return str(text).lower()

