import unittest
import HTMLTestRunner

testsuit=unittest.TestLoader().discover('.')
filename="E:/report/res.html"
f=open(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='redmine report',description='this is a redmine report')
runner.run(testsuit)
f.close()


