import unittest
from selenium import webdriver
import time
question='abc{}'.format(time.time())
class add_question(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost/redmine/login')
        self.driver.find_element_by_id('username').send_keys("user")
        self.driver.find_element_by_id('password').send_keys("12345678")
        self.driver.find_element_by_name('login').click()
        self.driver.get('http://localhost/redmine/projects/project1/issues')

    def test_add_question(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/a').click()
        self.driver.find_element_by_id('issue_subject').send_keys(question)
        self.driver.find_element_by_xpath('//*[@id="issue-form"]/input[3]').click()
        self.assertIn('已创建',self.driver.page_source)
    def tearDown(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/a[5]').click()
        self.driver.switch_to.alert.accept()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
