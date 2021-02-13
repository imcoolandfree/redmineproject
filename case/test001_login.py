import unittest
from selenium import webdriver
from time import sleep

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost/redmine/login')
    def test_login(self):
        self.driver.find_element_by_id('username').send_keys("user")
        self.driver.find_element_by_id('password').send_keys("12345678")
        self.driver.find_element_by_name('login').click()
        ele=self.driver.find_element_by_xpath('//*[@id="loggedas"]/a')
        self.assertEqual('user',ele.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

