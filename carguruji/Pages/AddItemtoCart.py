from selenium.webdriver.support.ui import Select

class add_to_cart():

    def __init__(self, driver):
        self.driver = driver

        self.women_click_xpath = "//a[@class='sf-with-ul'][contains(text(),'Women')]"
        self.tops_click_xpath = "//div[@id='subcategories']//li[1]//div[1]//a[1]//img[1]"
        self.blouses_click_xpath = "//div[@id='subcategories']//li[2]//div[1]//a[1]//img[1]"
        self.selectblouse_click_xpath = "//a[@class='product_img_link']//img[@class='replace-2x img-responsive']"
        self.addtocart_click_xpath="//span[contains(text(),'Add to cart')]"
        self.proceed_tocheckout1click_xpath = "//span[contains(text(),'Proceed to checkout')]"
        self.proceed_tocheckout2click_xpath = "//a[@class='button btn btn-default standard-checkout button-medium']//span[contains(text(),'Proceed to checkout')]"
        self.addressco_textbox_xpath="//input[@id='address1']"
        self.city_textbox_xpath="//input[@id='city']"
        self.state_dropdown_xpath="//select[@id='id_state']"#Alaska
        self.zipcode_textbox_xpath="//input[@id='postcode']"
        self.country_dropdown_xpath="//select[@id='id_country']"
        self.phone_textbox_xpath="//input[@id='phone']"
        self.mobile_textbox_xpath="//input[@id='phone_mobile']"
        self.addresstitle_asitis_xpath="//input[@id='alias']"
        self.save_click_xpath="//span[contains(text(),'Save')]"
        self.checkout1_xpath = "//button[@name='processAddress']//span[contains(text(),'Proceed to checkout')]"
        self.agreeterms_click_xpath="//input[@id='cgv']"
        self.checkout2_xpath = "//button[@name='processCarrier']//span[contains(text(),'Proceed to checkout')]"
        self.paybycheck_click_xpath = "//a[@class='cheque']"
        self.confirm_click_xpath = "//span[contains(text(),'I confirm my order')]"
        #screenshot

    def click_women(self):
        self.driver.find_element_by_xpath(self.women_click_xpath).click()
    def click_tops(self):
        self.driver.find_element_by_xpath(self.tops_click_xpath).click()
    def click_blouses(self):
        self.driver.find_element_by_xpath(self.blouses_click_xpath).click()
    def click_selectblouse(self):
        self.driver.find_element_by_xpath(self.selectblouse_click_xpath).click()
    def click_addtocart(self):
        self.driver.find_element_by_xpath(self.addtocart_click_xpath).click()
    def click_proceedcheckout1(self):
        self.driver.find_element_by_xpath(self.proceed_tocheckout1click_xpath).click()
    def click_proceedcheckout2(self):
        self.driver.find_element_by_xpath(self.proceed_tocheckout2click_xpath).click()
    def click_address(self,addressco):
        self.driver.find_element_by_xpath(self.addressco_textbox_xpath).send_keys(addressco)
    def click_city(self,city):
        self.driver.find_element_by_xpath(self.city_textbox_xpath).send_keys(city)
    def click_state(self,state):
        element = self.driver.find_element_by_xpath(self.state_dropdown_xpath)
        drop = Select(element)
        drop.select_by_visible_text(state)
    def click_postalcode(self,zipcode):
        self.driver.find_element_by_xpath(self.zipcode_textbox_xpath).send_keys(zipcode)
    def click_country(self,country):
        element = self.driver.find_element_by_xpath(self.country_dropdown_xpath)
        drop = Select(element)
        drop.select_by_visible_text(country)
    def click_phonenumber(self,phoneno):
        self.driver.find_element_by_xpath(self.phone_textbox_xpath).send_keys(phoneno)
    def click_mobilenumber(self,mobileno):
        self.driver.find_element_by_xpath(self.mobile_textbox_xpath).send_keys(mobileno)
    def click_save(self):
        self.driver.find_element_by_xpath(self.save_click_xpath).click()
    def click_checkout1(self):
        self.driver.find_element_by_xpath(self.checkout1_xpath).click()
    def click_terms(self):
        self.driver.find_element_by_xpath(self.agreeterms_click_xpath).click()
    def click_checkout2(self):
        self.driver.find_element_by_xpath(self.checkout2_xpath).click()
    def click_paybycheck(self):
        self.driver.find_element_by_xpath(self.paybycheck_click_xpath).click()
    def click_confirmorder(self):
        self.driver.find_element_by_xpath(self.confirm_click_xpath).click()

