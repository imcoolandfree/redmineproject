from selenium.webdriver.common.by import By
'''
登录页面
'''
class loginpagelocator():
    Username=(By.ID,'username') #登录名
    PassWord=(By.ID,'password')#登录密码
    login=(By.NAME,'login')#登录按钮
    loginIn=(By.XPATH,'//*[@id="loggedas"]/a')#已登录成功用户名
'''
新建用户页面
'''
class userpagelocator():
    userlogin=(By.XPATH,'//*[@id="content"]/div[1]/a')#新建用户
    loginname=(By.ID,'user_login')
    userfirstname=(By.ID,'user_firstname')#用户第一个名
    userlastname=(By.ID,'user_lastname')#用户最后一个名
    usermail=(By.ID,'user_mail')#用户邮箱
    userpassword=(By.ID,'user_password')#用户登录密码
    user_password_confirmation=(By.ID,'user_password_confirmation')#用户登录密码重复操作
    userin=(By.XPATH,'//*[@id="new_user"]/p[2]/input[1]')#用户创建成功名
    search=(By.ID,'name')#搜索新建用户名
    application=(By.XPATH,'//*[@id="users_form"]/fieldset/input[2]')#应用按钮
    delete=(By.XPATH,'//*[@id="content"]/div[2]/table/tbody/tr/td[8]/a[2]')#删除用户名称

'''
新建项目页面
'''
class projectpagelocator():
    projectbutton=(By.XPATH,'//*[@id="content"]/div[1]/a[1]')#新建项目
    projectname=(By.ID,'project_name')#项目名称
    addproject=(By.XPATH,'//*[@id="new_project"]/input[3]')#创建项目
    search=(By.ID,'name')#搜索项目
    application=(By.XPATH,'//*[@id="content"]/form/fieldset/input[2]')#应用按钮
    delete=(By.XPATH,'//*[@id="content"]/div[2]/table/tbody/tr/td[4]/a[3]')#删除项目
    confirm=(By.ID,'confirm')#确认按钮
    deletebutton=(By.XPATH,'//*[@id="content"]/form/p/input')#删除项目再次确认

'''
问题列表页面
'''
class buglistpagelocator():
    newquestion=(By.XPATH,'//*[@id="content"]/div[1]/a')#新建问题
    delete=(By.XPATH,'//*[@id="content"]/div[2]/a[5]')#删除问题

class newquestionpagelocator():
    questionname=(By.ID,'issue_subject')#新建问题名称
    addquestion=(By.XPATH,'//*[@id="issue-form"]/input[3]')#创建问题按钮



