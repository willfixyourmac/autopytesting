import unittest
import HtmlTestRunner
from POM.Pages.Homepg import HomePage
from POM.Pages.Loginpg import LoginPage
from POM.Drivers.Driver import chromedriver
from POM.Screenshots import scrn
from POM import Reports

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = chromedriver
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("http://www.newtours.demoaut.com/")
        login = LoginPage(driver)
        login.enter_username("mercury")
        login.enter_password("mercury")
        login.click_login()
        y = driver.title
        print (y)
        if y !=("Find a Flight: Mercury Tours:"):
            return ("unable to login, please try again")
        else:
            scrn.scrnsht(self)
            logout = HomePage(driver)
            logout.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=(HtmlTestRunner.HTMLTestRunner(output=Reports, verbosity=2)))
