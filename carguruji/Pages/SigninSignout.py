class in_out():

    def __init__(self,driver):
        self.driver = driver
        self.click_signin1_xpath = "//a[@class='login']"
        self.enteremail_signin_xpath = "//input[@id='email']"
        self.enterpassword_signin_xpath = "//input[@id='passwd']"
        self.click_signin2_xpath = "//form[@id='login_form']//span[1]"
        self.click_signout_xpath = "//a[@class='logout']"

    def click_signin1(self):
        self.driver.find_element_by_xpath(self.click_signin1_xpath).click()
    def enter_email(self,signinemail):
        self.driver.find_element_by_xpath(self.enteremail_signin_xpath).send_keys(signinemail)
    def enter_password(self,signinpassword):
        self.driver.find_element_by_xpath(self.enterpassword_signin_xpath).send_keys(signinpassword)
    def click_signin2(self):
        self.driver.find_element_by_xpath(self.click_signin2_xpath).click()
    def click_signout(self):
        self.driver.find_element_by_xpath(self.click_signout_xpath).click()
