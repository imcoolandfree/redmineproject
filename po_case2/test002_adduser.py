import unittest
from selenium import webdriver
from time import sleep
import time
from po_case2.redmine_page import *

username='user{}'.format(time.time())
email='{}@163.com'.format(username)
class add_user_test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost/redmine/login')
        loginpage = LoginPage(self.driver)
        loginpage.enter_username()
        loginpage.enter_password()
        loginpage.click_login()
        self.driver.get("http://localhost/redmine/users")

    def test_adduser(self):
        adduserpage=AddUserPage(self.driver)
        adduserpage.new_user()
        adduserpage.enter_name(username)
        adduserpage.enter_firstname()
        adduserpage.enter_lastname()
        adduserpage.enter_mail(email)
        adduserpage.enter_pwd()
        adduserpage.enter_pwd2()
        adduserpage.click_user()
        self.assertIn('已创建', self.driver.page_source)

    def tearDown(self):
        self.driver.get("http://localhost/redmine/users")
        adduserpage = AddUserPage(self.driver)
        adduserpage.search_user()
        adduserpage.click_user2()
        adduserpage.delete_user()
        self.driver.switch_to.alert.accept()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()