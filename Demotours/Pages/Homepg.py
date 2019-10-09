class HomePage():

    def __init__(self,driver):
        self.driver = driver
        self.sign_on_xpath ="//a[contains(text(),'SIGN-ON')]"
        self.register_xpath ="//a[contains(text(),'REGISTER')]"
        self.support_xpath = "//a[contains(text(),'SUPPORT')]"
        self.contact_xpath = "//body//td[4]"
        self.logout_button_xpath = "//a[contains(text(),'SIGN-OFF')]"

    def click_sign_on(self):
        self.driver.find_element_by_xpath(self.sign_on_xpath).click()

    def click_register(self):
        self.driver.find_element_by_xpath(self.register_xpath).click()

    def click_support(self):
        self.driver.find_element_by_xpath(self.support_xpath).click()

    def click_contact(self):
        self.driver.find_element_by_xpath(self.contact_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()

        // input[ @ id = 'email']