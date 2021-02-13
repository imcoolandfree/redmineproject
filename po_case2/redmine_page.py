from po_case2.redmine_locator import *

class basepage():
    def __init__(self,driver):
        self.driver=driver

class LoginPage(basepage):
    '''用户登录页面元素操作'''
    def enter_username(self):
        ele=self.driver.find_element(*loginpagelocator.Username)
        ele.send_keys('user')
    def enter_password(self):
        ele=self.driver.find_element(*loginpagelocator.PassWord)
        ele.send_keys('12345678')
    def click_login(self):
        ele=self.driver.find_element(*loginpagelocator.login)
        ele.click()
    def login_in(self):
        ele=self.driver.find_element(*loginpagelocator.loginIn)
        return ele.text

class AddUserPage(basepage):
    '''新增用户页面'''
    def new_user(self):
        ele=self.driver.find_element(*userpagelocator.userlogin)
        ele.click()
    def enter_name(self,username):
        ele=self.driver.find_element(*userpagelocator.loginname)
        ele.send_keys(username)
    def enter_firstname(self):
        ele=self.driver.find_element(*userpagelocator.userfirstname)
        ele.send_keys('a')
    def enter_lastname(self):
        ele=self.driver.find_element(*userpagelocator.userlastname)
        ele.send_keys('b')
    def enter_mail(self,email):
        ele=self.driver.find_element(*userpagelocator.usermail)
        ele.send_keys(email)
    def enter_pwd(self):
        ele=self.driver.find_element(*userpagelocator.userpassword)
        ele.send_keys('12345678')
    def enter_pwd2(self):
        ele=self.driver.find_element(*userpagelocator.user_password_confirmation)
        ele.send_keys('12345678')
    def click_user(self):
        ele=self.driver.find_element(*userpagelocator.userin)
        ele.click()
    def search_user(self):
        ele=self.driver.find_element(*userpagelocator.search)
        ele.click()
    def click_user2(self):
        ele=self.driver.find_element(*userpagelocator.application)
        ele.click()
    def delete_user(self):
        ele=self.driver.find_element(*userpagelocator.delete)
        ele.click()

class AddProjectPage(basepage):
    '''新建项目页面'''
    def addproject(self):
        ele=self.driver.find_element(*projectpagelocator.projectbutton)
        ele.click()
    def enter_project_name(self,projectname):
        ele=self.driver.find_element(*projectpagelocator.projectname)
        ele.send_keys(projectname)
    def click_project(self):
        ele=self.driver.find_element(*projectpagelocator.addproject)
        ele.click()
    def search_project(self,projectname):
        ele=self.driver.find_element(*projectpagelocator.search)
        ele.send_keys(projectname)
    def click_addproject(self):
        ele=self.driver.find_element(*projectpagelocator.application)
        ele.click()
    def delete_project(self):
        ele=self.driver.find_element(*projectpagelocator.delete)
        ele.click()
    def delete_confirm(self):
        ele=self.driver.find_element(*projectpagelocator.confirm)
        ele.click()
    def deletebutton(self):
        ele=self.driver.find_element(*projectpagelocator.deletebutton)
        ele.click()

class BugPage(basepage):
    def add_bug(self):
        ele=self.driver.find_element(*buglistpagelocator.newquestion)
        ele.click()
    def delete_question(self):
        ele=self.driver.find_element(*buglistpagelocator.delete)
        ele.click()

class AddBugPage(basepage):
    def add_question_name(self,question):
        ele=self.driver.find_element(*newquestionpagelocator.questionname)
        ele.send_keys(question)
    def click_addquestion(self):
        ele=self.driver.find_element(*newquestionpagelocator.addquestion)
        ele.click()
