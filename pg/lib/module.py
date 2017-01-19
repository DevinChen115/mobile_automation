import util
import os
import sys
sys.path.append(os.path.abspath(os.pardir)+"/res")
import PG_element as el

parentFolder = os.path.abspath(os.pardir)

class Module:
    def __init__(self, mDevice, dir):
        self.driver = mDevice
        self.util = util.Util(self.driver, dir)

    def loginByEmail(self):
        self.util.waitUntilAndGetElement("id",el.FivePage['profile'],"Try to go profile page").click()
        self.util.waitUntilAndGetElement("id",el.ProfilePage['Mail'],"Try to click email").click()
        self.util.waitUntilAndGetElement("id",el.emailLoginPage['account'],"Try to click account").click()
        util.osCommand('adb shell input text yan.work.tw@gmail.com')
        self.util.waitUntilAndGetElement("id",el.emailLoginPage['pwd'],"Try to click passowrd").click()
        util.osCommand('adb shell input text pgtest')
        self.util.waitUntilAndGetElement("id",el.emailLoginPage['submit'],"Try to click submit").click()
        return self.util.waitUntilAndGetElement("id",el.ProfilePageAfterLogin['nickName'],"Try to get Nick Name")