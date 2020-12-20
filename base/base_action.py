from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element, timeout=30, poll_frequency=0.5):
        # 用显示等待
        return WebDriverWait(driver=self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda x: x.find_element(*element))

    def find_elements(self, element, timeout=30, poll_frequency=0.5):
        # 用显示等待
        return WebDriverWait(driver=self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda x: x.find_elements(*element))

    def base_click(self, element):
        self.find_element(element).click()

    def base_send_keys(self, element, value):
        q = self.find_element(element=element)
        #     清空
        # q.clear()
        #     填写值
        q.send_keys(value)

    def base_get_text_info(self, element):
        return self.find_element(element=element).text

    def base_just_swip(self, direction="dtu"):
        print("当前页面没有要找的元素，进行滑动")
        # 获取手机的分辩率来后计算滑动距离,这样就能灵活适应大部分机型的分辨率到时候不用再修改代码
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]

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
            self.driver.swipe(up_x, up_y, down_x, down_y, 3000)
        # 从下往上
        elif direction == "dtu":
            self.driver.swipe(down_x, down_y, up_x, up_y, 3000)
        # 从左往右
        elif direction == "ltr":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        # 从右往左
        elif direction == "rtl":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        else:
            raise Exception("只能【从左往右:ltr】【从右往左:rtl】【从上往下:utd】【从下往右上:dtu】}")

    def base_assert_toast_info(self, msg):
        '''
        查找toast信息
        :param msg:
        :return:
        ''',
        toast_info = By.XPATH, "//*[contains(@text,'%s')]" % msg
        try:
            self.find_element(element=toast_info)
            return True
        except Exception:
            return False

    def base_get_toast(self, message):
        """
        根据 部分内容，获取toast上的所有内容
        :param message: 部分内容
        :return: 所有内容
        """
        if self.base_assert_toast_info(msg=message):
            message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
            return self.find_element(message_xpath).text
        else:
            raise Exception("toast未出现，请检查参数是否正确或toast有没有出现在屏幕上")

    # 判断元素是否存在
    def base_is_element_existence(self, element):
        try:
            self.find_element(element=element)
            return True
        except Exception:
            return False

    def base_swip_to_somewhere(self, msg, direction="dtu"):
        page_source = ""
        while True:
            # for i in range(4):
            try:
                element = By.XPATH, "//*[contains(@text,'%s')]" % msg
                return self.find_element(element)
                # 找到元素就停止循环，没找就执行Exception中的代码

            #     如果没有这个元素，才进行滑动操作，可以利用for或者while循环加上try来实现
            except Exception:
                self.base_just_swip(direction)
                # 判断是否滑动到底，每次滑动都将当前页面的东西赋值给一个变量，然后对比当前页面是否和赋值的变量相同，如果相同，就代表滑动到了底部，就终止滑动
                if self.driver.page_source == page_source:
                    print("已经滑动到最低了，没有东西了")
                    break
                # driver.page_source = page_source
                page_source = self.driver.page_source
