from google_result import ResultPage

from base import BasePage

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    GoogleSearchField = (By.XPATH, ".//*[@id='sb_ifc0']")
    GoogleSearchButton = (By.XPATH, ".//*[@id='sblsbb']")
    
    def inputKeyword(self, word):
    	self.wait.until(EC.presence_of_element_located(HomePage.GoogleSearchField))
        self.driver.find_element(*HomePage.GoogleSearchField).send_keys(word)

    def clickSearch(self):
        self.driver.find_element(*HomePage.GoogleSearchButton).click()
        return ResultPage(self.driver, self.wait)




