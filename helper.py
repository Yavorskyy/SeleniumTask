from selenium.webdriver.common.by import By

class HelpPage(object):
	
	GoogleSearchResult = (By.TAG_NAME, "body")
	def __init__(self, driver):
		self.driver = driver

	def getTextFromSearchResult(self):
		data_from_page = self.driver.find_elements(*HelpPage.GoogleSearchResult) # all data within webpage
		text = [comment.text for comment in data_from_page] # all this data put into the list
		return str(text).lower()
