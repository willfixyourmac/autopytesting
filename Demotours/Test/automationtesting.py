import unittest
import HtmlTestRunner
from POM import Reports
from POM.Drivers.Driver import chromedriver
from POM.Pages.hmpage import HomePage
from POM.Pages.register import RegisterPage
from POM.Screenshots import scrn
from POM.Pages.Orderpg import OrderPage


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = chromedriver
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test1_sign_up(self):
        driver = self.driver
        driver.get("http://demo.automationtesting.in/")
        driver.implicitly_wait(5)
        homepage = HomePage(driver)
        homepage.click_sign_up()
        driver.implicitly_wait(5)
        reg = RegisterPage(driver)
        reg.enter_firstname("Ali")
        reg.enter_lastname("Aliyev")
        reg.enter_adress("Adress1")
        reg.enter_email("test@mail.com")
        reg.enter_phone("6477777777")
        reg.click_male()
        reg.click_cricket()
        reg.select_language()
        reg.select_skills()
        reg.select_countries1()
        reg.select_countries2()
        reg.select_year()
        reg.select_month()
        reg.select_day()
        reg.enter_password("Testpass1")
        reg.confirm_password("Testpass1")
        reg.click_submit()
        driver.implicitly_wait(20)

    def test2_weborder(self):
        driver = self.driver
        driver.implicitly_wait(20)
        driver.get("http://practice.automationtesting.in/")
        order = OrderPage(driver)
        order.click_practice_page()
        scrn.scrnsht(self)
        driver.implicitly_wait(5)
        order.click_add_to_cart()
        order.click_cart()
        order.click_checkout()
        order.enter_firstname("Ali")
        order.enter_lastname("Aliyev")
        order.enter_company_name("CAC")
        order.enter_email("tst@mail.com")
        order.enter_phone("6477777777")
        order.select_country()
        order.enter_adress("adress1")
        order.enter_city()
        order.select_province()
        order.enter_postalcode("l4e0b4")
        order.select_payment()
        order.place_order()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=(HtmlTestRunner.HTMLTestRunner(output=Reports, verbosity=2)))
