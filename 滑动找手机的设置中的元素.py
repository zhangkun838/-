from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_action import BaseAction

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.254.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# desired_caps['automationName'] = 'Uiautomator2'
# desired_caps['noReset'] = True
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(time_to_wait=10)

a = BaseAction(driver)


def just_swip(direction):
    print("当前页面没有要找的元素，进行滑动")
    # 获取手机的分辩率来后计算滑动距离,这样就能灵活适应大部分机型的分辨率到时候不用再修改代码
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]

    # 计算出中间点方便运算
    center_x = width / 2
    center_y = height / 2

    left_x = width / 4 * 1
    left_y = center_y
    right_x = width / 4 * 3
    right_y = center_y

    # up：上；dowen:下
    up_x = center_x
    up_y = height / 4 * 1
    down_x = center_x
    down_y = height / 4 * 3

    # 从上往下
    if direction == "utd":
        driver.swipe(up_x, up_y, down_x, down_y, 3000)
    # 从下往上
    elif direction == "dtu":
        driver.swipe(down_x, down_y, up_x, up_y, 3000)
    # 从左往右
    elif direction == "ltr":
        driver.swipe(left_x, left_y, right_x, right_y, 3000)
    # 从右往左
    elif direction == "rtl":
        driver.swipe(right_x, right_y, left_x, left_y, 3000)
    else:
        raise Exception("只能【从左往右:ltr】【从右往左:rtl】【从上往下:utd】【从下往右上:dtu】}")


# 可以利用for循环进行多次的滑动，正常操作来讲，应该先去找看看当前的页面是否有这个元素，
def swip_to_somewhere(msg, direction, timeout=10, poll_frequency=0.1):
    page_source = ""
    while True:
        # for i in range(4):
        try:
            element = By.XPATH, "//*[contains(@text,'%s')]" % msg
            return WebDriverWait(driver=driver, timeout=timeout, poll_frequency=poll_frequency).until(
                lambda x: x.find_element(*element))
            # 找到元素就停止循环，没找就执行Exception中的代码

        #     如果没有这个元素，才进行滑动操作，可以利用for或者while循环加上try来实现
        except Exception:
            just_swip(direction)
            # 判断是否滑动到底，每次滑动都将当前页面的东西赋值给一个变量，然后对比当前页面是否和赋值的变量相同，如果相同，就代表滑动到了底部，就终止滑动
            if driver.page_source == page_source:
                print("已经滑动到最低了，没有东西了")
                break
            # driver.page_source = page_source
            page_source = driver.page_source


# sleep(3)

swip_to_somewhere(msg="关于手机", direction="dtu").click()
sleep(3)
driver.quit()
