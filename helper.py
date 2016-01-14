class HelpPage(object):

	def getTextFromSearchResult(self, locator_body):
		data_from_page = self.driver.find_elements(*locator_body) # all data within webpage
		text = [comment.text for comment in data_from_page] # all this data put into the list
		return str(text).lower()
