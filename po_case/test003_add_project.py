import unittest
from selenium import webdriver
from time import sleep
import time

projectname='project{}'.format(time.time())
class add_project(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost/redmine/login')
        self.driver.find_element_by_id('username').send_keys("user")
        self.driver.find_element_by_id('password').send_keys("12345678")
        self.driver.find_element_by_name('login').click()
        self.driver.get('http://localhost/redmine/projects')

    def test_addprotect(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/a[1]').click()
        self.driver.find_element_by_id('project_name').send_keys(projectname)
        self.driver.find_element_by_xpath('//*[@id="new_project"]/input[3]').click()
        self.assertIn('创建成功',self.driver.page_source)

    def tearDown(self):
        self.driver.get('http://localhost/redmine/admin/projects')
        self.driver.find_element_by_id('name').send_keys(projectname)
        self.driver.find_element_by_xpath('//*[@id="content"]/form/fieldset/input[2]').click()
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/table/tbody/tr/td[4]/a[3]').click()
        self.driver.find_element_by_id('confirm').click()
        self.driver.find_element_by_xpath('//*[@id="content"]/form/p/input').click()
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()