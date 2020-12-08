from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element, timeout=30, poll_frequency=0.5):
        # 用显示等待
        return WebDriverWait(driver=self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda x: x.find_element(*element))

    def base_click(self, element):
        self.find_element(element).click()

    def base_send_keys(self, element, value):
        q = self.find_element(element=element)
        #     清空
        q.clear()
        #     填写值
        q.send_keys(value)
