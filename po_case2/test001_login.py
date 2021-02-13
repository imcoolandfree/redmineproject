import unittest
from selenium import webdriver
from time import sleep
from po_case2.redmine_page import *

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost/redmine/login')
    def test_login(self):
        loginpage=LoginPage(self.driver)
        loginpage.enter_username()
        loginpage.enter_password()
        loginpage.click_login()
        self.assertEqual('user',loginpage.login_in())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

