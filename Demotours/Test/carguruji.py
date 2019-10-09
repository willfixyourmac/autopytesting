import unittest
import HtmlTestRunner
from POM.Drivers.Driver import chromedriver
from POM.Screenshots import scrn
from POM import Reports
from POM.Pages.AddItemtoCart import add_to_cart
from POM.Pages.SigninSignout import in_out

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = chromedriver
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()


    def test1_sign_in(self):
        driver = self.driver
        driver.get("http://carguruji.com/shop/login?back=my-account")
        driver.implicitly_wait(5)
        inout = in_out(driver)
        inout.click_signin1()
        inout.enter_email("test1@mail.com")
        inout.enter_password("Test1234")
        inout.click_signin2()
        driver.implicitly_wait(5)
        scrn.scrnsht1(self)

    def test2_addtocart(self):
        driver = self.driver
        inout = in_out(driver)
        cart = add_to_cart(driver)
        cart.click_women()
        driver.implicitly_wait(5)
        cart.click_tops()
        driver.implicitly_wait(5)
        cart.click_blouses()
        driver.implicitly_wait(5)
        driver.execute_script("window.scrollBy(0,1000)", "")
        cart.click_selectblouse()
        driver.implicitly_wait(5)
        cart.click_addtocart()
        driver.implicitly_wait(5)
        cart.click_proceedcheckout1()
        driver.implicitly_wait(5)
        cart.click_proceedcheckout2()
        driver.implicitly_wait(5)
        cart.click_address("adress1")
        cart.click_city("Alabaster")
        cart.click_state("Alabama")
        cart.click_postalcode("35007")
        cart.click_country("United States")
        cart.click_phonenumber("6477777777")
        cart.click_mobilenumber("6477777777")
        cart.click_save()
        cart.click_checkout1()
        cart.click_terms()
        cart.click_checkout2()
        driver.execute_script("window.scrollBy(0,1000)", "")
        cart.click_paybycheck()
        cart.click_confirmorder()
        scrn.scrnsht1(self)
        inout.click_signout()
        title = driver.title
        self.assertEqual("Login - CarGuruji Shop", title,)

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=(HtmlTestRunner.HTMLTestRunner(output=Reports, verbosity=2)))
