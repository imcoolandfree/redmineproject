import unittest
from selenium import webdriver
from time import sleep
import time

username='user{}'.format(time.time())
class add_user_test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost/redmine/login')
        self.driver.find_element_by_id('username').send_keys("user")
        self.driver.find_element_by_id('password').send_keys("12345678")
        self.driver.find_element_by_name('login').click()
        self.driver.get("http://localhost/redmine/users")

    def test_adduser(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/a').click()
        self.driver.find_element_by_id('user_login').send_keys(username)
        self.driver.find_element_by_id('user_firstname').send_keys('a')
        self.driver.find_element_by_id('user_lastname').send_keys('b')
        self.driver.find_element_by_id('user_mail').send_keys('{}@163.com'.format(username))
        self.driver.find_element_by_id('user_password').send_keys('12345678')
        self.driver.find_element_by_id('user_password_confirmation').send_keys('12345678')
        self.driver.find_element_by_xpath('//*[@id="new_user"]/p[2]/input[1]').click()
        self.assertIn('已创建',self.driver.page_source)

    def tearDown(self):
        self.driver.get("http://localhost/redmine/users")
        self.driver.find_element_by_id('name').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="users_form"]/fieldset/input[2]').click()
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/table/tbody/tr/td[8]/a[2]').click()
        self.driver.switch_to.alert.accept()
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()