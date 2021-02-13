import unittest
from selenium import webdriver
import time
from po_case2.redmine_page import *

question='abc{}'.format(time.time())
class add_question(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost/redmine/login')
        loginpage = LoginPage(self.driver)
        loginpage.enter_username()
        loginpage.enter_password()
        loginpage.click_login()
        self.driver.get('http://localhost/redmine/projects/project1/issues')

    def test_add_question(self):
        bugpage=BugPage(self.driver)
        addbugpage=AddBugPage(self.driver)
        bugpage.add_bug()
        addbugpage.add_question_name(question)
        addbugpage.click_addquestion()
        self.assertIn('已创建',self.driver.page_source)
    def tearDown(self):
        bugpage = BugPage(self.driver)
        bugpage.delete_question()
        self.driver.switch_to.alert.accept()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
