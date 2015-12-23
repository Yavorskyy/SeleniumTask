class ResultPage(object):
    def __init__(self, driver):
        self.driver = driver
    
    def clickGoogleSearchResult(self, row_number):
    	self.driver.find_element_by_xpath(".//*[@id='rso']/div/div[{}]/div/h3/a".format(row_number)).click()

    def n_link(self):
        data_from_page = self.driver.find_elements_by_class_name('body') # all data within webpage
        text = [comment.text for comment in data_from_page] # all this data put into the list
        return str(text)
