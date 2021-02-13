import unittest
from selenium import webdriver
from time import sleep
import time
from po_case2.redmine_page import *

projectname='project{}'.format(time.time())
class add_project(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost/redmine/login')
        loginpage = LoginPage(self.driver)
        loginpage.enter_username()
        loginpage.enter_password()
        loginpage.click_login()
        self.driver.get('http://localhost/redmine/projects')

    def test_addprotect(self):
        addprojectpage=AddProjectPage(self.driver)
        addprojectpage.addproject()
        addprojectpage.enter_project_name(projectname)
        addprojectpage.click_project()
        self.assertIn('创建成功',self.driver.page_source)

    def tearDown(self):
        self.driver.get('http://localhost/redmine/admin/projects')
        addprojectpage = AddProjectPage(self.driver)
        addprojectpage.search_project(projectname)
        addprojectpage.click_addproject()
        addprojectpage.delete_project()
        addprojectpage.delete_confirm()
        addprojectpage.deletebutton()
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()