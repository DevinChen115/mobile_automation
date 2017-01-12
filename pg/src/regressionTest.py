import os
import time
import unittest
from appium import webdriver

import sys
sys.path.append(os.path.abspath(os.pardir)+"/lib")
sys.path.append(os.path.abspath(os.pardir)+"/res")
import util as ul
import HTMLTestRunner
import PG_element as el


# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

parentFolder = os.path.abspath(os.pardir)

def PATH(p):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), p))


def checkFolder():
        if not os.path.exists( parentFolder + "/result"):
            os.makedirs(parentFolder + "/result")


# Result = dict (Manufacturer,Model,Brand,Androidversion,SDKversion,SerialNo)
Result = ul.getDeviceStatus()


class regression_test(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = Result["Androidversion"]
        desired_caps['deviceName'] = Result["SerialNo"]
        desired_caps['appPackage'] = el.Package['appPackage']
        desired_caps['appActivity'] = el.Package['appActivity']

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.pgutil = ul.Util(self.driver, parentFolder + "/screenshots")

    def tearDown(self):
        self.driver.quit()

    def test_FirstTimeLaunchNeedHaveLoginPage(self):
        try:
            if(self.pgutil.clearDate()):
                self.pgutil.launchPG()
                isHaveSkip = self.pgutil.isEleClickable(el.LoginPage['skip'])
                isHaveTopImg = self.pgutil.isEleClickable(el.LoginPage['topImage'])
                isHaveMore = self.pgutil.isEleClickable(el.LoginPage['more'])
                if((isHaveMore) and (isHaveSkip) and (isHaveTopImg)):
                    self.assertTrue(True)
            else:
                raise
        except:
            self.pgutil.screenshot("test_FirstTimeLaunchNeedHaveLoginPage")
            self.assertTrue(False)


if __name__ == '__main__':
    checkFolder()
    suite = unittest.TestLoader().loadTestsFromTestCase(regression_test)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    file = open(str(PATH(parentFolder+'/result/' + str(time.strftime("%Y%m%d") + '.html'))), "wb")
    
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=file,
        title="[PG Automation] [Python+Appium] [Device: " + ' ' + Result["Manufacturer"] + ' ' + Result["Model"] + ' ' + Result["Brand"] + ']',
        description="[Platform Version: " + Result["Androidversion"] + ']' + "[SDK version: " + Result["SDKversion"] + ']' + "[Device S/N: " + Result["SerialNo"] + ']')
    runner.run(suite)
    
    file.close()
