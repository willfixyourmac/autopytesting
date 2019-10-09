

class LoginPage():

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox_xpath = "//input[@name='userName']"
        self.password_textbox_xpath = "//input[@name='password']"
        self.login_button_xpath = "//input[@name='login']"




    def enter_username(self,username):
        #self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)
        self.driver.implicitly_wait(10)

    def enter_password(self,password):
        #self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)
        self.driver.implicitly_wait(10)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

