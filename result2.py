from locator import ResultLocator



class ResultPage(object):
    def __init__(self, driver):
        self.driver = driver
    
    def clickGoogleSearchResult(self, row_number):
    	locator_for_row = ResultLocator.GoogleSearchResult #locator with result rows on google page(from GoogleSearchResults class)
    	list_for_locator = [] #create list
    	list_for_locator = list(locator_for_row) #locator change from tuple to list
    	list_for_locator[1] = list_for_locator[1].format(row_number) #enter needed number of row in locator xpath
    	locator_for_row = tuple(list_for_locator) # back from list to tuple for locator   	
        self.driver.find_element(*locator_for_row).click() #click needed result row


    def getTextFromPage(self):
        data_from_page = self.driver.find_elements(*ResultLocator.Page) # all data within webpage
        text = [comment.text for comment in data_from_page] # all this data put into the list
        return str(text).lower()
