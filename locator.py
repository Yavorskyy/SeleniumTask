from selenium.webdriver.common.by import By

class HomeLocator(object):
	GoogleSearchField = (By.XPATH, ".//*[@id='sb_ifc0']")
	GoogleSearchButton = (By.XPATH, ".//*[@id='sblsbb']")

class ResultLocator(object):
	
	TenSearchResults = (By.XPATH, "//*[@id='rso']//h3/a")
	GoogleSearchResult = (By.XPATH, ".//*[@id='rso']/div/div[{}]/div/h3/a")
	Page = (By.TAG_NAME, "body")