import openpyxl
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import logging
import HtmlTestRunner
import DDT.XLUtils
#driver = webdriver.Chrome (executable_path="/Users/yu/Downloads/chromedriver-2")
from POM.Pages.loginPage import LoginPage
from POM.Pages.homePage import HomePage

class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome (executable_path="/Users/yu/Downloads/chromedriver-2")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver =self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")

        login=LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main(testRunner=(HtmlTestRunner.HTMLTestRunner(output="/Users/yu/Desktop", verbosity=2)))
