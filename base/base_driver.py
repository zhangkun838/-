from appium import webdriver

'''
包名界面名：com.android.mms/.ui.ConversationList
'''


class BaseDriver:
    # 前置代码设置,因为别的大部分应用多是要登陆的状态，所以在这里不让应用重置，如果需要的化直接传False
    def get_driver(self, noReset=True):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.254.101:5555'
        desired_caps['appPackage'] = 'com.yunmall.lc'
        desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
        desired_caps['automationName'] = 'Uiautomator2'
        desired_caps['noReset'] = noReset
        return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
