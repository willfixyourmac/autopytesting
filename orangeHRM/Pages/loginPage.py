

class LoginPage():

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox_xpath = "//input[@id='txtUsername']"
        self.password_textbox_xpath = "//input[@id='txtPassword']"
        self.login_button_xpath = "//input[@id='btnLogin']"
        #self.forgot_password_xpath = "//a[contains(text(),'Forgot your password?')]"
        #self.main_page_xpath = "//a[contains(text(),'OrangeHRM, Inc')]"
        #self.linkedin_xpath = "//a[1]//img[1]"
        #self.facebook_xpath = "//a[2]//img[1]"
        #self.twitter_xpath = "//a[3]//img[1]"
        #self.youtube_xpath = "//a[4]//img[1]"


    def enter_username(self,username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)
        self.driver.implicitly_wait(10)

    def enter_password(self,password):
        #self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)
        self.driver.implicitly_wait(10)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

