

class HomePage():

    def __init__(self,driver):
        self.driver = driver
        self.welcome_xpath = "//a[@id='welcome']"
        self.logout_xpath = "//a[contains(text(),'Logout')]"
        self.about_xpath = "//a[@id='aboutDisplayLink']"

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()

    def click_about(self):
        self.driver.find_element_by_xpath(self.about_xpath).click()

    def click_welcome(self):
        self.driver.find_element_by_xpath(self.welcome_xpath).click()

