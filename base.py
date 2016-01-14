from helper import HelpPage

class  BasePage(HelpPage):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

