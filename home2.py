from result2 import ResultPage

class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
    
    def inputKeyword(self, param):
        self.driver.find_element_by_xpath(".//*[@id='sb_ifc0']").send_keys(param)
        #return HomePage(self.driver)

    def clickSearch(self):
        self.driver.find_element_by_xpath(".//*[@id='sblsbb']").click()
        return ResultPage(self.driver)


'''
    def search(self, param):
        self.driver.find_element_by_xpath(".//*[@id='sb_ifc0']").send_keys(param) #in google search window enter data from TestPage class('python v.3.5')
        
        self.driver.find_element_by_xpath(".//*[@id='sblsbb']").click() # can be deleted if will work without pushing button
        
        self.n = 5
        self.driver.find_element_by_xpath(".//*[@id='rso']/div/div[{}]/div/h3/a".format(self.n)).click() #click n link within search result
        return ResultPage(self.driver)
'''




